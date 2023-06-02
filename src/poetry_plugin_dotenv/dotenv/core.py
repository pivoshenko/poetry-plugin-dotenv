"""Module that contains core dotenv functionality."""

from __future__ import annotations

import io
import os
import sys
import typing
import contextlib

from collections import OrderedDict

from poetry_plugin_dotenv.dotenv import parsers
from poetry_plugin_dotenv.dotenv import variables


class DotEnv:
    """Model of a dotenv file."""

    def __init__(
        self,
        filepath: str | None = None,
        stream: typing.IO[str] | None = None,
        interpolate: bool = True,
        override: bool = True,
    ) -> None:
        """Initialize."""

        self.stream = stream
        self.override = override
        self.filepath = filepath
        self.interpolate = interpolate

        self.encoding = "utf-8"

        self._dict: typing.OrderedDict[str, str] | None = None

    def dict(self) -> typing.OrderedDict[str, str]:  # noqa: A003
        """Return content of a dotenv file."""

        if self._dict:
            return self._dict

        raw_values = self.parse()

        if self.interpolate:
            self._dict = resolve(raw_values, override=self.override)

        else:
            self._dict = OrderedDict(raw_values)

        return self._dict

    def parse(self) -> typing.Generator:
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

        return False  # pragma: nocover

    @contextlib.contextmanager
    def _get_stream(self) -> typing.Iterator[typing.IO[str]]:
        """Get a dotenv stream."""

        if self.filepath and os.path.isfile(self.filepath):
            with open(self.filepath, encoding=self.encoding) as stream:
                yield stream

        elif self.stream:
            yield self.stream

        else:
            yield io.StringIO("")  # pragma: nocover


def resolve(
    values: typing.Iterable[tuple[str, str]],
    override: bool,
) -> typing.OrderedDict[str, str]:
    """Resolve dotenv variables."""

    new_values: typing.OrderedDict[str, str] = OrderedDict()

    for name, value in values:
        if value is None:
            result = None  # pragma: nocover

        else:
            atoms = variables.parse(value)
            env: typing.OrderedDict[str, str] = OrderedDict()

            if override:
                env.update(os.environ)
                env.update(new_values)

            else:
                env.update(new_values)
                env.update(os.environ)

            result = "".join(atom.resolve(env) for atom in atoms)

        new_values[name] = result

    return new_values


def walk_to_root(path: str) -> typing.Iterator[str]:
    """Yield directories starting from the given directory up to the root."""

    if not os.path.exists(path):
        msg = "Starting path not found."
        raise OSError(msg)  # pragma: nocover

    if os.path.isfile(path):
        path = os.path.dirname(path)  # pragma: nocover

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

    else:  # pragma: no cover
        frame = sys._getframe()  # noqa: SLF001
        current_file = __file__

        while frame.f_code.co_filename == current_file:
            # S101 - this asserts is part of the original package
            assert frame.f_back is not None  # noqa: S101
            frame = frame.f_back

        frame_filename = frame.f_code.co_filename
        path = os.path.dirname(os.path.abspath(frame_filename))

    for dirname in walk_to_root(path):
        check_path = os.path.join(dirname, filename)

        if os.path.isfile(check_path):
            return check_path

    return ""


def load(
    filepath: str | None = None,
    stream: typing.IO[str] | None = None,
    interpolate: bool = True,
    override: bool = True,
) -> bool:
    """Parse a dotenv file and then load all the variables found as environment variables."""

    dotenv = DotEnv(
        filepath=filepath,
        interpolate=interpolate,
        override=override,
        stream=stream,
    )
    return dotenv.set_as_environment_variables()


def values(
    filepath: str | None = None,
    stream: typing.IO[str] | None = None,
    interpolate: bool = True,
) -> typing.OrderedDict[str, str]:
    """Parse a dotenv file and return its content as a dictionary."""

    return DotEnv(filepath=filepath, stream=stream, interpolate=interpolate).dict()
