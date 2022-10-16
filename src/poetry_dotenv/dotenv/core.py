"""Module that contains core dotenv functionality."""

import io
import os
import sys
import contextlib

from collections import OrderedDict
from typing import IO
from typing import Iterable
from typing import Iterator
from typing import Optional
from typing import Tuple

from poetry_dotenv.dotenv import parsers
from poetry_dotenv.dotenv import variables


class DotEnv(object):
    """Model of a dotenv file."""

    def __init__(
        self,
        filepath: str,
        stream: Optional[IO[str]] = None,
        interpolate: bool = True,
        override: bool = True,
    ) -> None:
        """Initialize."""

        self.stream = stream
        self.override = override
        self.filepath = filepath
        self.interpolate = interpolate

        self.encoding = "utf-8"

        self._dict: Optional[OrderedDict[str, Optional[str]]] = None

    def dict(self) -> OrderedDict[str, Optional[str]]:
        """Return content of a dotenv file."""

        if self._dict:
            return self._dict

        raw_values = self.parse()

        if self.interpolate:
            self._dict = resolve(raw_values, override=self.override)

        else:
            self._dict = OrderedDict(raw_values)

        return self._dict

    def parse(self) -> Iterator[Tuple[str, Optional[str]]]:
        """Parse a dotenv file."""

        with self._get_stream() as stream:
            for mapping in parsers.parse_stream(stream):
                if mapping.key is not None:
                    yield mapping.key, mapping.value

    def set_as_environment_variables(self) -> bool:
        """Load current dotenv as a system environment variable."""

        if self.dict():
            for key, value in self.dict().items():

                if key in os.environ and not self.override:
                    continue

                if value:
                    os.environ[key] = value

            return True

        return False

    @contextlib.contextmanager
    def _get_stream(self) -> Iterator[IO[str]]:
        """Get a dotenv stream."""

        if self.filepath and os.path.isfile(self.filepath):
            with open(self.filepath, encoding=self.encoding) as stream:
                yield stream

        elif self.stream:
            yield self.stream

        else:
            yield io.StringIO("")


def resolve(
    values: Iterable[Tuple[str, Optional[str]]],
    override: bool,
) -> OrderedDict[str, Optional[str]]:
    """Resolve dotenv variables."""

    new_values: OrderedDict[str, Optional[str]] = OrderedDict()

    for (name, value) in values:
        if value is None:
            result = None

        else:
            atoms = variables.parse(value)
            env: OrderedDict[str, Optional[str]] = OrderedDict()

            if override:
                env.update(os.environ)
                env.update(new_values)

            else:
                env.update(new_values)
                env.update(os.environ)

            result = "".join(atom.resolve(env) for atom in atoms)

        new_values[name] = result

    return new_values


def walk_to_root(path: str) -> Iterator[str]:
    """Yield directories starting from the given directory up to the root."""

    if not os.path.exists(path):
        raise IOError("Starting path not found.")  # pragma: no cover

    if os.path.isfile(path):
        path = os.path.dirname(path)

    last_dir = None
    current_dir = os.path.abspath(path)

    while last_dir != current_dir:
        yield current_dir
        parent_dir = os.path.abspath(os.path.join(current_dir, os.path.pardir))
        last_dir, current_dir = current_dir, parent_dir


def find(filename: str = ".env", usecwd: bool = False) -> str:
    """Search in increasingly higher folders for the given file."""

    if usecwd or getattr(sys, "frozen", False):
        path = os.getcwd()

    else:
        # WPS437 - call of a protected method is a only way to get a frame
        frame = sys._getframe()  # noqa: WPS437
        current_file = __file__

        while frame.f_code.co_filename == current_file:
            # S101 - this assert is part of the original package
            assert frame.f_back is not None  # noqa: S101
            frame = frame.f_back

        frame_filename = frame.f_code.co_filename
        path = os.path.dirname(os.path.abspath(frame_filename))

    for dirname in walk_to_root(path):
        check_path = os.path.join(dirname, filename)

        if os.path.isfile(check_path):
            return check_path

    return ""


def load(filepath: str, interpolate: bool = True, override: bool = False) -> bool:
    """Parse a dotenv file and then load all the variables found as environment variables."""

    dotenv = DotEnv(
        filepath=filepath,
        interpolate=interpolate,
        override=override,
    )
    return dotenv.set_as_environment_variables()


def values(filepath: str, interpolate: bool = True) -> OrderedDict[str, Optional[str]]:
    """Parse a dotenv file and return its content as a dictionary."""

    return DotEnv(filepath=filepath, interpolate=interpolate).dict()
