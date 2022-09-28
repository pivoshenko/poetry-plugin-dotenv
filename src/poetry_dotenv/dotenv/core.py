"""Module that contains core dotenv functionality."""

import io
import os
import sys
import contextlib

from collections import OrderedDict
from typing import Dict
from typing import IO
from typing import Iterable
from typing import Iterator
from typing import Optional
from typing import Tuple
from typing import Union

from poetry_dotenv.dotenv.parsers import parse_stream
from poetry_dotenv.dotenv.variables import parse_variables


class DotEnv(object):
    """Model of a dotenv file."""

    def __init__(
        self,
        dotenv_path: Optional[str] = None,
        stream: Optional[IO[str]] = None,
        encoding: Union[None, str] = None,
        interpolate: bool = True,
        override: bool = True,
    ) -> None:
        """Initialize."""

        self.dotenv_path = dotenv_path
        self.stream = stream
        self.encoding = encoding
        self.interpolate = interpolate
        self.override = override

        self._dict: Optional[OrderedDict[str, Optional[str]]] = None

    def dict(self) -> Dict[str, Optional[str]]:
        """Return dotenv file as a dictionary."""

        if self._dict:
            return self._dict

        raw_values = self.parse()

        if self.interpolate:
            self._dict = OrderedDict(resolve_variables(raw_values, override=self.override))

        else:
            self._dict = OrderedDict(raw_values)

        return self._dict

    def parse(self) -> Iterator[Tuple[str, Optional[str]]]:
        """Parse dotenv file."""

        with self._get_stream() as stream:
            for mapping in parse_stream(stream):
                if mapping.key is not None:
                    yield mapping.key, mapping.value

    def set_as_environment_variables(self) -> bool:
        """Load current dotenv as a system environment variable."""

        if not self.dict():  # pragma: no cover
            return False

        for key, value in self.dict().items():

            if key in os.environ and not self.override:
                continue

            if value is not None:
                os.environ[key] = value

        return True

    def get(self, key: str) -> Optional[str]:  # pragma: no cover
        """Get a dotenv variable."""

        data = self.dict()

        return data.get(key)

    @contextlib.contextmanager
    def _get_stream(self) -> Iterator[IO[str]]:
        """Get a dotenv stream."""

        if self.dotenv_path and os.path.isfile(self.dotenv_path):
            with open(self.dotenv_path, encoding=self.encoding) as stream:
                yield stream

        elif self.stream is not None:
            yield self.stream

        else:
            yield io.StringIO("")  # pragma: no cover


def resolve_variables(
    values: Iterable[Tuple[str, Optional[str]]],
    override: bool,
) -> Dict[str, Optional[str]]:
    """Resolve dotenv variables."""

    new_values: Dict[str, Optional[str]] = {}

    for (name, value) in values:
        if value is None:
            result = None  # pragma: no cover

        else:
            atoms = parse_variables(value)
            env: Dict[str, Optional[str]] = {}

            if override:
                env.update(os.environ)  # type: ignore
                env.update(new_values)

            else:
                env.update(new_values)
                env.update(os.environ)  # type: ignore

            result = "".join(atom.resolve(env) for atom in atoms)

        new_values[name] = result

    return new_values


def walk_to_root(path: str) -> Iterator[str]:
    """Yield directories starting from the given directory up to the root."""

    if not os.path.exists(path):
        raise IOError("Starting path not found.")  # pragma: no cover

    if os.path.isfile(path):
        path = os.path.dirname(path)  # pragma: no cover

    last_dir = None
    current_dir = os.path.abspath(path)

    while last_dir != current_dir:
        yield current_dir
        parent_dir = os.path.abspath(os.path.join(current_dir, os.path.pardir))
        last_dir, current_dir = current_dir, parent_dir


def find_dotenv(
    filename: str = ".env",
    raise_error_if_not_found: bool = False,
    usecwd: bool = False,
) -> str:
    """Search in increasingly higher folders for the given file."""

    # S101, WPS437 - `find_dotenv` is a legacy function

    if usecwd or getattr(sys, "frozen", False):
        path = os.getcwd()

    else:  # pragma: no cover
        # noinspection PyUnresolvedReferences,PyProtectedMember
        frame = sys._getframe()  # noqa: WPS437
        current_file = __file__

        while frame.f_code.co_filename == current_file:
            assert frame.f_back is not None  # noqa: S101
            frame = frame.f_back

        frame_filename = frame.f_code.co_filename
        path = os.path.dirname(os.path.abspath(frame_filename))

    for dirname in walk_to_root(path):
        check_path = os.path.join(dirname, filename)

        if os.path.isfile(check_path):
            return check_path

    if raise_error_if_not_found:
        raise IOError("File not found.")

    return ""


def load_dotenv(
    dotenv_path: Optional[str] = None,
    stream: Optional[IO[str]] = None,
    override: bool = False,
    interpolate: bool = True,
    encoding: Optional[str] = "utf-8",
) -> bool:
    """Parse a dotenv file and then load all the variables found as environment variables."""

    if dotenv_path is None and stream is None:
        dotenv_path = find_dotenv()  # pragma: no cover

    dotenv = DotEnv(
        dotenv_path=dotenv_path,
        stream=stream,
        interpolate=interpolate,
        override=override,
        encoding=encoding,
    )
    return dotenv.set_as_environment_variables()


def dotenv_values(
    dotenv_path: Optional[str] = None,
    stream: Optional[IO[str]] = None,
    interpolate: bool = True,
    encoding: Optional[str] = "utf-8",
) -> Dict[str, Optional[str]]:
    """Parse a dotenv file and return its content as a dictionary."""

    if dotenv_path is None and stream is None:
        dotenv_path = find_dotenv()  # pragma: no cover

    return DotEnv(
        dotenv_path=dotenv_path,
        stream=stream,
        interpolate=interpolate,
        encoding=encoding,
    ).dict()
