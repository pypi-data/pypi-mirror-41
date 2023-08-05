# Copyright (c) 2016-present, Facebook, Inc.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.


import argparse
import itertools
import json
import logging
import os
import pathlib
import re
import subprocess
import sys
import traceback
from collections import defaultdict
from typing import Any, Dict, List, Optional, Tuple

from .commands import ExitCode
from .filesystem import get_filesystem


LOG = logging.getLogger(__name__)


def json_to_errors(json_string: Optional[str]) -> List[Dict[str, Any]]:
    if json_string:
        try:
            return json.loads(json_string)
        except json.decoder.JSONDecodeError:
            LOG.error(
                "Recevied invalid JSON as input."
                "If piping from `pyre check` be sure to use `--output=json`."
            )
    else:
        LOG.error(
            "Recevied no input."
            "If piping from `pyre check` be sure to use `--output=json`."
        )
    return []


class Configuration:
    def __init__(self, path: str, json_contents: Dict[str, Any]):
        self._path = path
        if path.endswith("/.pyre_configuration.local"):
            self.is_local = True
        else:
            self.is_local = False
        self.root = os.path.dirname(path)
        self.targets = json_contents.get("targets")
        self.source_directories = json_contents.get("source_directories")
        self.push_blocking = bool(json_contents.get("push_blocking"))

    @staticmethod
    def find_project_configuration() -> Optional[str]:
        directory = os.getcwd()
        while directory != "/":
            configuration_path = os.path.join(directory, ".pyre_configuration")
            if os.path.isfile(configuration_path):
                return configuration_path
            directory = os.path.dirname(directory)
        return None

    @staticmethod
    def gather_local_configurations(arguments) -> List["Configuration"]:
        LOG.info("Finding configurations...")
        configuration_paths = get_filesystem().list(".", ".pyre_configuration.local")
        if not configuration_paths:
            LOG.info("No projects with local configurations found.")
            project_configuration = Configuration.find_project_configuration()
            if project_configuration:
                configuration_paths = [project_configuration]
            else:
                LOG.error("No project configuration found.")
                return []
        configurations = []
        for configuration_path in configuration_paths:
            with open(configuration_path) as configuration_file:
                configuration = Configuration(
                    configuration_path, json.load(configuration_file)
                )
                if configuration.push_blocking or (not arguments.push_blocking_only):
                    configurations.append(configuration)
        return configurations

    def get_path(self) -> str:
        return self._path

    def remove_version(self) -> None:
        with open(self._path) as configuration_file:
            contents = json.load(configuration_file)
        if "version" not in contents:
            LOG.info("Version not found in configuration.")
            return
        del contents["version"]
        with open(self._path, "w") as configuration_file:
            json.dump(contents, configuration_file, sort_keys=True, indent=2)
            configuration_file.write("\n")

    def get_errors(self) -> List[Dict[str, Any]]:
        # TODO(T37074129): Better parallelization or truncation needed for fbcode
        if self.targets:
            try:
                # If building targets, run clean or space may run out on device!
                LOG.info("Running `buck clean`...")
                subprocess.call(["buck", "clean"], timeout=200)
            except subprocess.TimeoutExpired as error:
                LOG.warning("Buck timed out. Try running `buck kill` before retrying.")
                return []
            except subprocess.CalledProcessError as error:
                LOG.warning("Error calling `buck clean`: %s", str(error))
                return []
        try:
            LOG.info("Checking `%s`...", self.root)
            if self.is_local:
                process = subprocess.run(
                    ["pyre", "-l", self.root, "--output=json", "check"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
            else:
                process = subprocess.run(
                    ["pyre", "--output=json", "check"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
            json_string = process.stdout.decode().strip()
            errors = json_to_errors(json_string)
            LOG.info("Found %d error%s.", len(errors), "s" if len(errors) != 1 else "")
            return errors
        except subprocess.CalledProcessError as error:
            LOG.warning("Error calling pyre: %s", str(error))
            return []


def errors_from_configurations(arguments) -> List[Dict[str, Any]]:
    configurations = Configuration.gather_local_configurations(arguments)
    LOG.info(
        "Found %d %sconfiguration%s",
        len(configurations),
        "push-blocking " if arguments.push_blocking_only else "",
        "s" if len(configurations) != 1 else "",
    )
    total_errors = []
    for configuration in configurations:
        total_errors += configuration.get_errors()
    return total_errors


def errors_from_stdin(_arguments) -> List[Dict[str, Any]]:
    input = sys.stdin.read()
    return json_to_errors(input)


def partition_on_any_delimiter(
    string: str, delimiters: List[str]
) -> Tuple[str, str, str]:
    prefix = ""
    delimiter = ""
    suffix = ""
    for index, char in enumerate(string):
        if char in delimiters:
            delimiter = str(char)
            suffix = string[index + 1 :]
            break
        prefix += char

    return prefix, delimiter, suffix


def generate_full_comment(
    max_line_length: Optional[int], indent: str, codes: List[str], description: str
) -> List[str]:
    prefix = "{}# pyre-fixme[{}]: ".format(indent, ", ".join(codes))
    comment = prefix + description

    if (
        not max_line_length
        or len(comment) <= max_line_length
        # If the prefix is too long, there is no way we can split this description.
        or len(prefix) > max_line_length
    ):
        return [comment]

    preamble_prefix = indent + "# pyre: "
    # Even if the preamble prefix is definitely shorter than the prefix, use the
    # length of the prefix to determine the available columns for ease of
    # implementation.
    available_columns = max_line_length - len(prefix)

    buffered_line = ""
    result = []
    while len(description):
        token, delimiter, remaining = partition_on_any_delimiter(
            description, delimiters=[" ", "."]
        )

        if buffered_line and (
            len(buffered_line) + len(token) + len(delimiter) > available_columns
        ):
            # This new token would make the line exceed the limit,
            # hence terminate what we have accumulated.
            result.append((preamble_prefix + buffered_line).rstrip())
            buffered_line = ""

        buffered_line = buffered_line + token + delimiter
        description = remaining

    result.append((prefix + buffered_line).rstrip())
    return result


def remove_comment_preamble(lines: List[str]) -> None:
    while lines:
        old_line = lines.pop()
        new_line = re.sub(r"# pyre: .*$", "", old_line).rstrip()
        if old_line == "" or new_line != "":
            # The preamble has ended.
            lines.append(new_line)
            return


def fix(
    arguments: argparse.Namespace,
    filename: str,
    codes: Dict[int, str],
    descriptions: Dict[int, str],
) -> None:
    custom_comment = arguments.comment if hasattr(arguments, "comment") else ""
    max_line_length = (
        arguments.max_line_length if arguments.max_line_length > 0 else None
    )
    path = pathlib.Path(filename)
    lines = path.read_text().split("\n")  # type: List[str]

    # Replace lines in file.
    new_lines = []
    for index, line in enumerate(lines):
        number = index + 1
        if number in codes:
            if list(codes[number]) == ["0"]:
                # Handle unused ignores.
                replacement = re.sub(r"# pyre-(ignore|fixme).*$", "", line).rstrip()
                if replacement == "":
                    remove_comment_preamble(new_lines)
                else:
                    new_lines.append(replacement)
                continue

            sorted_codes = sorted(list(codes[number]))
            sorted_descriptions = sorted(list(descriptions[number]))

            description = (
                custom_comment if custom_comment else " ".join(sorted_descriptions)
            )

            full_comment = generate_full_comment(
                max_line_length,
                line[: (len(line) - len(line.lstrip(" ")))],  # indent
                sorted_codes,
                description,
            )
            LOG.info("Adding comment on line %d: %s", number, "\n".join(full_comment))
            new_lines.extend(full_comment)

        new_lines.append(line)

    path.write_text("\n".join(new_lines))


# Exposed for testing.
def _upgrade_configuration(
    arguments: argparse.Namespace, configuration: Configuration, root: str
) -> None:
    LOG.info("Processing %s", configuration.get_path())
    if not configuration.is_local:
        return
    configuration.remove_version()
    errors = configuration.get_errors()
    if len(errors) == 0:
        return

    def error_path(error):
        return error["path"]

    errors = itertools.groupby(sorted(errors, key=error_path), error_path)
    run_fixme(arguments, errors)
    try:
        LOG.info("Committing changes.")
        directory = os.path.relpath(os.path.dirname(configuration.get_path()), root)
        commit_message = "[typing] Update pyre version for {}".format(directory)
        subprocess.call(["hg", "commit", "--message", commit_message])
    except subprocess.CalledProcessError:
        LOG.info("Error while running hg.")


def run_fixme(
    arguments: argparse.Namespace, result: List[Tuple[str, List[Any]]]
) -> None:
    for path, errors in result:
        LOG.info("Processing `%s`", path)

        # Build map from line to error codes.
        codes = defaultdict(lambda: set())
        descriptions = defaultdict(lambda: set())
        for error in errors:
            match = re.search(r"\[(\d+)\]: (.*)", error["description"])
            if match:
                codes[error["line"]].add(match.group(1))
                descriptions[error["line"]].add(match.group(2))

        fix(arguments, path, codes, descriptions)


def run_global_version_update(
    arguments: argparse.Namespace, result: List[Tuple[str, List[Any]]]
) -> None:
    global_configuration = Configuration.find_project_configuration()
    if global_configuration is None:
        LOG.error("No global configuration file found.")
        return

    local_configurations = [
        configuration
        for configuration in Configuration.gather_local_configurations(arguments)
        if configuration.is_local
    ]

    with open(global_configuration, "r") as global_configuration_file:
        configuration = json.load(global_configuration_file)
        if "version" not in configuration:
            LOG.error(
                "Global configuration at %s has no version field.", global_configuration
            )
            return

        old_version = configuration["version"]

    # Rewrite.
    with open(global_configuration, "w") as global_configuration_file:
        configuration["version"] = arguments.hash

        # This will sort the keys in the configuration - we won't be clobbering comments
        # since Python's JSON parser disallows comments either way.
        json.dump(configuration, global_configuration_file, sort_keys=True, indent=2)
        global_configuration_file.write("\n")

    for configuration in local_configurations:
        path = configuration.get_path()
        if "mock_repository" in path:
            # Skip local configurations we have for testing.
            continue
        with open(path) as configuration_file:
            contents = json.load(configuration_file)
            if "version" in contents:
                LOG.info("Skipping %s as it already has a custom version field.", path)
                continue
            contents["version"] = old_version

        with open(path, "w") as configuration_file:
            json.dump(contents, configuration_file, sort_keys=True, indent=2)
            configuration_file.write("\n")


def run_missing_overridden_return_annotations(
    _arguments, result: List[Tuple[str, List[Any]]]
) -> None:
    for path, errors in result:
        LOG.info("Patching errors in `%s`.", path)
        errors = reversed(sorted(errors, key=lambda error: error["line"]))

        path = pathlib.Path(path)
        lines = path.read_text().split("\n")

        for error in errors:
            if error["code"] != 15:
                continue
            line = error["line"] - 1

            match = re.match(r".*`(.*)`\.", error["description"])
            if not match:
                continue
            annotation = match.groups()[0]

            # Find last closing parenthesis in after line.
            LOG.info("Looking at %d: %s", line, lines[line])
            while True:
                if "):" in lines[line]:
                    lines[line] = lines[line].replace("):", ") -> %s:" % annotation)
                    LOG.info("%d: %s", line, lines[line])
                    break
                else:
                    line = line + 1

        LOG.warn("Writing patched %s", str(path))
        path.write_text("\n".join(lines))


def run_fixme_all(
    arguments: argparse.Namespace, errors: List[Tuple[str, List[Any]]]
) -> None:
    configurations = Configuration.gather_local_configurations(arguments)
    LOG.info(
        "Found %d %sconfiguration%s",
        len(configurations),
        "push-blocking " if arguments.push_blocking_only else "",
        "s" if len(configurations) != 1 else "",
    )
    root = Configuration.find_project_configuration()
    if root is None:
        LOG.info("No project configuration found for the current directory.")
        return
    else:
        root = os.path.dirname(root)

    for configuration in configurations:
        _upgrade_configuration(arguments, configuration, root)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    parser.add_argument(
        "--max-line-length",
        default=88,
        type=int,
        help="Enforce maximum line length on new comments "
        + "(default: %(default)s, use 0 to disable)",
    )

    commands = parser.add_subparsers()

    # Subcommand: Fixme all errors inputted through stdin.
    fixme = commands.add_parser("fixme")
    fixme.set_defaults(errors=errors_from_stdin, function=run_fixme)
    fixme.add_argument("--comment", help="Custom comment after fixme comments")

    # Subcommand: Add annotations according to errors inputted through stdin.
    missing_overridden_return_annotations = commands.add_parser(
        "missing-overridden-return-annotations"
    )
    missing_overridden_return_annotations.set_defaults(
        errors=errors_from_stdin, function=run_missing_overridden_return_annotations
    )

    # Subcommand: Find and run pyre against all configurations,
    # and fixme all errors in each project.
    fixme_all = commands.add_parser("fixme-all")
    fixme_all.set_defaults(errors=lambda _arguments: [], function=run_fixme_all)
    fixme_all.add_argument(
        "-c", "--comment", help="Custom comment after fixme comments"
    )
    fixme_all.add_argument("-p", "--push-blocking-only", action="store_true")

    update_global_version = commands.add_parser("update-global-version")
    update_global_version.set_defaults(
        errors=(lambda arguments: []), function=run_global_version_update
    )
    update_global_version.add_argument("hash", help="Hash of new Pyre version.")
    update_global_version.add_argument(
        "-p", "--push-blocking-only", action="store_true"
    )
    # Initialize default values.
    arguments = parser.parse_args()
    if not hasattr(arguments, "function"):
        arguments.function = run_fixme
    if not hasattr(arguments, "errors"):
        arguments.errors = errors_from_stdin

    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG if arguments.verbose else logging.INFO,
    )

    try:
        exit_code = ExitCode.SUCCESS

        def error_path(error):
            return error["path"]

        result = itertools.groupby(
            sorted(arguments.errors(arguments), key=error_path), error_path
        )
        arguments.function(arguments, result)
    except Exception as error:
        LOG.error(str(error))
        LOG.info(traceback.format_exc())
        exit_code = ExitCode.FAILURE

    sys.exit(exit_code)
