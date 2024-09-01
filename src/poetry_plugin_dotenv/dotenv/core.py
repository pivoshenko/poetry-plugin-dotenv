"""Module that contains core dotenv functionality."""

from __future__ import annotations

import io
import os
import sys
import contextlib

from collections import OrderedDict
from typing import IO
from typing import TYPE_CHECKING

from poetry_plugin_dotenv.dotenv import parsers
from poetry_plugin_dotenv.dotenv import variables


if TYPE_CHECKING:  # pragma: no cover
    from collections.abc import Iterable
    from collections.abc import Iterator


class DotEnv:
    """Model of a dotenv file."""

    def __init__(
        self,
        filepath: str | None = None,
        stream: IO[str] | None = None,
        *,
        interpolate: bool = True,
        override: bool = True,
    ) -> None:
        """Initialize."""

        self.filepath = filepath
        self.stream = stream
        self.override = override
        self.interpolate = interpolate
        self.encoding = "utf-8"
        self._dict: OrderedDict[str, str] | None = None

    def dict(self) -> OrderedDict[str, str]:
        """Return content of a dotenv file."""

        if self._dict is None:
            raw_values = self.parse()
            self._dict = (
                resolve(raw_values, override=self.override)
                if self.interpolate
                else OrderedDict(raw_values)  # type: ignore[arg-type]
            )

        return self._dict

    def parse(self) -> Iterator[tuple[str, str | None]]:
        """Parse a dotenv file."""

        with self._get_stream() as stream:
            for mapping in parsers.parse_stream(stream):
                if mapping.key is not None:
                    yield mapping.key, mapping.value

    def set_as_environment_variables(self) -> bool:
        """Load current dotenv as system environment variables."""

        env_dict = self.dict()

        if not env_dict:
            return False

        for key, value in env_dict.items():
            if key in os.environ and not self.override:
                continue

            if value:
                os.environ[key] = value

        return True

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
    values: Iterable[tuple[str, str | None]],
    *,
    override: bool,
) -> OrderedDict[str, str]:
    """Resolve dotenv variables."""

    new_values: OrderedDict[str, str] = OrderedDict()
    env = OrderedDict(os.environ.copy()) if override else OrderedDict()

    for name, value in values:
        if value is not None:
            atoms = variables.parse(value)

            if not override:
                env.update(new_values)

            else:
                env = OrderedDict({**env, **new_values})

            resolved_value = "".join(atom.resolve(env) for atom in atoms)
            new_values[name] = resolved_value

    return new_values


def walk_to_root(path: str) -> Iterator[str]:
    """Yield directories starting from the given directory up to the root."""

    if not os.path.exists(path):
        msg = "Starting path not found."
        raise OSError(msg)

    current_dir = os.path.abspath(os.path.dirname(path) if os.path.isfile(path) else path)

    while True:
        yield current_dir
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

        if current_dir == parent_dir:
            break

        current_dir = parent_dir


def find(filename: str = ".env", *, usecwd: bool = False) -> str:
    """Search in increasingly higher folders for the given file."""

    path = (
        os.getcwd()
        if usecwd or getattr(sys, "frozen", False)
        else os.path.dirname(os.path.abspath(sys._getframe(1).f_code.co_filename))  # noqa: SLF001
    )

    for dirname in walk_to_root(path):
        check_path = os.path.join(dirname, filename)

        if os.path.isfile(check_path):
            return check_path

    return ""


def load(
    filepath: str | None = None,
    stream: IO[str] | None = None,
    *,
    interpolate: bool = True,
    override: bool = True,
) -> bool:
    """Parse a dotenv file and then load all the variables found as environment variables."""

    dotenv = DotEnv(filepath=filepath, interpolate=interpolate, override=override, stream=stream)
    return dotenv.set_as_environment_variables()


def values(
    filepath: str | None = None,
    stream: IO[str] | None = None,
    *,
    interpolate: bool = True,
) -> OrderedDict[str, str]:
    """Parse a dotenv file and return its content as a dictionary."""

    return DotEnv(filepath=filepath, stream=stream, interpolate=interpolate).dict()
