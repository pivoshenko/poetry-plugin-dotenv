"""Module that contains core dotenv functionality."""

from __future__ import annotations

import io
import os
import sys
import shlex
import contextlib
import subprocess

from collections import OrderedDict
from pathlib import Path
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
        filepath: str | Path | None = None,
        stream: IO[str] | None = None,
        *,
        interpolate: bool = True,
        override: bool = True,
    ) -> None:
        """Initialize."""
        self.filepath = Path(filepath) if isinstance(filepath, str) else filepath
        self.stream = stream
        self.override = override
        self.interpolate = interpolate
        self.encoding = "utf-8"
        self._dict: OrderedDict[str, str] | None = None

    def dict(self) -> OrderedDict[str, str]:
        """Get content of a dotenv file."""
        if self._dict:
            return self._dict

        raw_values = self.parse()

        if self.interpolate:
            self._dict = resolve(raw_values, override=self.override)

        else:
            self._dict = OrderedDict(raw_values)

        return self._dict

    def parse(self) -> Iterator[tuple[str, str]]:
        """Parse a dotenv file."""
        with self._get_stream() as stream:
            for mapping in parsers.parse_stream(stream):
                if mapping.key is not None:
                    yield mapping.key, mapping.value

    def set_as_environment_variables(self) -> bool:
        """Load current dotenv as system environment variables."""
        if self.dict():
            for key, value in self.dict().items():
                if key in os.environ and not self.override:
                    continue
                if value:
                    os.environ[key] = value

            return True

        return False  # pragma: nocover

    def set_in_shell(self) -> bool:
        """Set current dotenv in the shell."""
        if self.dict():
            for key, value in self.dict().items():
                if key in os.environ and not self.override:
                    continue
                if value:
                    escaped_value = shlex.quote(value)
                    command = f"export {key}={escaped_value}"
                    try:
                        subprocess.run(command, shell=True, check=True)  # noqa: S602
                    except subprocess.CalledProcessError:
                        return False

            return True

        return False  # pragma: nocover

    @contextlib.contextmanager
    def _get_stream(self) -> Iterator[IO[str]]:
        """Get a dotenv stream."""
        if self.filepath and self.filepath.is_file():
            with self.filepath.open(encoding=self.encoding) as stream:
                yield stream

        elif self.stream:
            yield self.stream

        else:
            yield io.StringIO("")  # pragma: nocover


def resolve(values: Iterable[tuple[str, str]], *, override: bool) -> OrderedDict[str, str]:
    """Resolve dotenv variables."""
    new_values: OrderedDict[str, str] = OrderedDict()

    for name, value in values:
        if value is None:
            result = None  # pragma: nocover

        else:
            atoms = variables.parse(value)
            env: OrderedDict[str, str] = OrderedDict()

            if override:
                env.update(os.environ)
                env.update(new_values)

            else:
                env.update(new_values)
                env.update(os.environ)

            result = "".join(atom.resolve(env) for atom in atoms)

        new_values[name] = result

    return new_values


def walk_to_root(path: str | Path) -> Iterator[Path]:
    """Yield directories starting from the given directory up to the root."""
    path_obj = Path(path) if isinstance(path, str) else path
    if not path_obj.exists():
        msg = "Starting path not found."
        raise OSError(msg)

    current_dir = path_obj.parent.resolve() if path_obj.is_file() else path_obj.resolve()

    while True:
        yield current_dir
        parent_dir = current_dir.parent

        if current_dir == parent_dir:
            break

        current_dir = parent_dir


def find(filename: str = ".env", *, usecwd: bool = False) -> Path | None:
    """Search in increasingly higher folders for the given file."""
    if usecwd or getattr(sys, "frozen", False):
        path = Path.cwd()
    else:
        # Get the directory of the caller's file
        caller_frame = sys._getframe(1)  # noqa: SLF001
        caller_file = Path(caller_frame.f_code.co_filename).resolve()
        path = caller_file.parent

    for dirname in walk_to_root(path):
        check_path = dirname / filename

        if check_path.is_file():
            return check_path

    return None


def load(
    filepath: str | Path | None = None,
    stream: IO[str] | None = None,
    *,
    interpolate: bool = True,
    override: bool = True,
) -> bool:
    """Parse a dotenv file and then load all the variables found as environment variables."""
    dotenv = DotEnv(filepath=filepath, interpolate=interpolate, override=override, stream=stream)
    return dotenv.set_as_environment_variables()


def values(
    filepath: str | Path | None = None,
    stream: IO[str] | None = None,
    *,
    interpolate: bool = True,
) -> OrderedDict[str, str]:
    """Parse a dotenv file and return its content as a dictionary."""
    return DotEnv(filepath=filepath, stream=stream, interpolate=interpolate).dict()
