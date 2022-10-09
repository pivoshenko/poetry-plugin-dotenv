"""Module that contains core dotenv IO functionality."""

import re
import sys

from pathlib import Path
from typing import Iterator
from typing import Pattern


def make_regex(expression: str, extra_flags: int = 0) -> Pattern[str]:
    """Construct a regex expression."""

    return re.compile(expression, re.UNICODE | extra_flags)


def walk_to_root(path: Path) -> Iterator[Path]:
    """Yield directories starting from the given directory up to the root."""

    if not path.exists():
        raise IOError("Starting path {0!r} not found.".format(path))

    dirpath = path.parent if path.is_file() else path

    last_dir = None
    current_dir = dirpath.absolute()

    while last_dir != current_dir:
        yield current_dir

        parent_dir = current_dir.parent.absolute()
        last_dir, current_dir = current_dir, parent_dir


def find_dotenv(
    filename: str = ".env",
    usecwd: bool = False,
    raise_error_if_not_found: bool = False,
) -> Path:
    """Search in increasingly higher directories for the given file."""

    path = _get_path(usecwd)

    for dirname in walk_to_root(path):
        check_path = dirname / filename

        if check_path.exists():
            return check_path

    if raise_error_if_not_found:
        raise IOError("File {0!r} not found.".format(filename))

    return Path()


def _get_path(usecwd: bool = False) -> Path:
    """Get a base path."""

    if usecwd or getattr(sys, "frozen", False):
        path = Path.cwd().absolute()

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
        path = Path(frame_filename).absolute()

    return path
