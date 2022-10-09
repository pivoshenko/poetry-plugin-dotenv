"""Module that contains core dotenv IO functionality."""

import re

from pathlib import Path
import sys
from types import FrameType
from typing import Iterator
from typing import Optional
from typing import Pattern


def make_regex(expression: str, extra_flags: int = 0) -> Pattern[str]:
    """Construct a regex expression."""

    return re.compile(expression, re.UNICODE | extra_flags)


def walk_to_root(path: Path) -> Iterator[Path]:
    """Yield directories starting from the given directory up to the root."""

    if not path.exists():
        raise IOError("Starting path {0!r} not found.".format(path))

    dirpath: Path = path.parent if path.is_file() else path

    last_dir: Optional[Path] = None
    current_dir: Path = dirpath.absolute()

    while last_dir != current_dir:
        yield current_dir

        parent_dir = current_dir.parent.absolute()
        last_dir, current_dir = current_dir, parent_dir


def find_dotenv(
    filename: str = ".env",
    raise_error_if_not_found: bool = False,
    usecwd: bool = False,
) -> Path:
    """Search in increasingly higher directories for the given file."""

    if usecwd or getattr(sys, "frozen", False):
        path: Path = Path.cwd()

    else:
        frame: FrameType = sys._getframe()  # noqa: WPS437
        current_file: str = __file__

        while frame.f_code.co_filename == current_file:
            assert frame.f_back is not None  # noqa: S101
            frame = frame.f_back

        frame_filename = frame.f_code.co_filename
        path = os.path.dirname(os.path.abspath(frame_filename))
