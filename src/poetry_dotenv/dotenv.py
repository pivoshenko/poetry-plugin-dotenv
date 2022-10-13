"""Module that contains core dotenv functionality."""

import os
import re
import sys

from pathlib import Path
from typing import Iterator
from typing import Optional
from typing import OrderedDict
from typing import Pattern

from returns.result import Failure
from returns.result import Result
from returns.result import Success
from returns.result import safe


Dotenv = Optional[OrderedDict[str, str]]


def find(filename: str = ".env", usecwd: bool = False) -> Result[Path, FileNotFoundError]:
    """Search in increasingly higher directories for a given dotenv file."""

    base_path = _get_base_path(usecwd)

    for dirname in _walk_to_root(base_path):
        filepath = dirname / filename

        if filepath.exists():
            return Success(filepath)

    return Failure(FileNotFoundError("File {0!r} not found.".format(filename)))


def load(filepath: Path) -> Result[Dotenv, FileNotFoundError]:
    """Parse and get a content of a dotenv file."""

    filepath = filepath if filepath else Path()
    filepath = Path(filepath) if isinstance(filepath, str) else filepath

    if filepath.is_file():
        # WPS322 - we need a triple quotes for the next regex expression
        parser = _make_regex(r"""^([^=]+)\s+?=\s+?(?:[\s"']*)(.+?)(?:[\s"']*)$""")  # noqa: WPS322
        dotenv = OrderedDict()

        with open(filepath, encoding="utf-8") as stream:
            for line in stream:
                match = parser.match(line)
                if match:
                    dotenv[match.group(1)] = match.group(2)

        return Success(dotenv)

    return Failure(FileNotFoundError("File {0!r} not found.".format(filepath)))


def set_as_environment_variables(dotenv: Dotenv, override: bool) -> Result[None, ValueError]:
    """Set the content of a dotenv file as the system environment variables."""

    if dotenv:
        # WPS110 - `value` is a good name in the such context
        for key, value in dotenv.items():  # noqa: WPS110
            if key in os.environ and not override:
                continue

            if value:
                os.environ[key] = value

        return Success(None)

    return Failure(ValueError("The content of a dotenv file is empty."))


@safe
def _make_regex(expression: str, extra_flags: int = 0) -> Pattern[str]:
    """Construct a regex expression."""

    return re.compile(expression, re.UNICODE | extra_flags)


def _walk_to_root(path: Path) -> Result[Iterator[Path], FileNotFoundError]:
    """Yield directories starting from the given directory up to the root."""

    if not path.exists():
        return Failure(FileNotFoundError("Starting path {0!r} not found.".format(path)))

    dirpath = path.parent if path.is_file() else path

    last_dir = Path()
    current_dir = dirpath.absolute()

    while last_dir != current_dir:
        yield Success(current_dir)

        parent_dir = current_dir.parent.absolute()
        last_dir, current_dir = current_dir, parent_dir


def _get_base_path(usecwd: bool = False) -> Path:
    """Get a base path."""

    if usecwd or getattr(sys, "frozen", False):
        base_path = Path.cwd().absolute()

    else:
        # WPS437 - the protected method is the only way to get a frame object from the call stack
        frame = sys._getframe()  # noqa: WPS437
        current_file = __file__

        while frame.f_code.co_filename == current_file:
            if frame.f_back:
                frame = frame.f_back

            else:
                raise ValueError("Frame {0!r} is None.".format(frame.f_back))

        frame_filename = frame.f_code.co_filename
        base_path = Path(frame_filename).absolute()

    return base_path
