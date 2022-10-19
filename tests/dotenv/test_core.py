"""Tests for the module ``src/poetry_update/dotenv/core.py``."""

import io
import os
import sys
import textwrap

from pathlib import Path
from typing import Dict
from unittest import mock

import sh
import pytest

from poetry_dotenv.dotenv import core as dotenv


def prepare_file_hierarchy(path: Path):
    """Create a temporary folder structure like the following.

    test_find_dotenv0/
    └── child1
    ├──── child2
    │   └── child3
    │       └── child4
    └── .env

    Then try to automatically ``find_dotenv`` starting in ``child4``.
    """

    curr_dir = path
    dirs = []
    for filepath in ("child1", "child2", "child3", "child4"):
        curr_dir /= filepath
        dirs.append(curr_dir)
        curr_dir.mkdir()

    return dirs[0], dirs[-1]


def test_find_dotenv_no_file_no_raise(tmp_path: Path) -> None:
    """Test ``find`` function."""

    *_, leaf = prepare_file_hierarchy(tmp_path)
    os.chdir(str(leaf))

    result = dotenv.find(usecwd=True)

    assert result == ""


def test_find_dotenv_found(tmp_path: Path) -> None:
    """Test ``find`` function."""

    (root, leaf) = prepare_file_hierarchy(tmp_path)
    os.chdir(str(leaf))
    dotenv_file = root / ".env"
    dotenv_file.write_bytes(b"TEST=test\n")

    result = dotenv.find(usecwd=True)

    assert result == str(dotenv_file)


@mock.patch.dict(os.environ, {}, clear=True)
def test_load_dotenv_existing_file(dotenv_file: str) -> None:
    """Test ``load`` function."""

    with open(dotenv_file, "w") as env_file:
        env_file.write("a=b")

    result = dotenv.load(dotenv_file)

    assert result is True
    assert os.environ == {"a": "b"}


@mock.patch.dict(os.environ, {"a": "c"}, clear=True)
def test_load_dotenv_existing_variable_no_override(dotenv_file: str) -> None:
    """Test ``load`` function."""

    with open(dotenv_file, "w") as env_file:
        env_file.write("a=b")

    result = dotenv.load(dotenv_file, override=False)

    assert result is True
    assert os.environ == {"a": "c"}


@mock.patch.dict(os.environ, {"a": "c"}, clear=True)
def test_load_dotenv_existing_variable_override(dotenv_file: str) -> None:
    """Test ``load`` function."""

    with open(dotenv_file, "w") as env_file:
        env_file.write("a=b")

    result = dotenv.load(dotenv_file)

    assert result is True
    assert os.environ == {"a": "b"}


@mock.patch.dict(os.environ, {"a": "c"}, clear=True)
def test_load_dotenv_redefine_var_used_in_file_no_override(dotenv_file: str) -> None:
    """Test ``load`` function."""

    with open(dotenv_file, "w") as env_file:
        env_file.write('a=b\nd="${a}"')

    result = dotenv.load(dotenv_file, override=False)

    assert result is True
    assert os.environ == {"a": "c", "d": "c"}


@mock.patch.dict(os.environ, {"a": "c"}, clear=True)
def test_load_dotenv_redefine_var_used_in_file_with_override(dotenv_file: str) -> None:
    """Test ``load`` function."""

    with open(dotenv_file, "w") as env_file:
        env_file.write('a=b\nd="${a}"')

    result = dotenv.load(dotenv_file, override=True)

    assert result is True
    assert os.environ == {"a": "b", "d": "b"}


@mock.patch.dict(os.environ, {}, clear=True)
def test_load_dotenv_string_io():
    """Test ``load`` function."""

    stream = io.StringIO("a=à")

    result = dotenv.load(stream=stream)

    assert result is True
    assert os.environ == {"a": "à"}


@mock.patch.dict(os.environ, {}, clear=True)
def test_load_dotenv_file_stream(dotenv_file: str) -> None:
    """Test ``load`` function."""

    with open(dotenv_file, "w") as env_file:
        env_file.write("a=b")

    with open(dotenv_file, "r") as env_file:
        result = dotenv.load(stream=env_file)

    assert result is True
    assert os.environ == {"a": "b"}


def test_load_dotenv_in_current_dir(tmp_path: Path) -> None:
    """Test ``load`` function."""

    dotenv_path = tmp_path / ".env"
    dotenv_path.write_bytes(b"a=b")
    code_path = tmp_path / "code.py"
    code_path.write_text(
        textwrap.dedent(  # noqa: WPS462
            """
            from poetry_dotenv.dotenv import core as dotenv
            import os
            dotenv.load(dotenv.find())
            print(os.environ['a'])
        """,
        ),
    )
    os.chdir(str(tmp_path))

    result = sh.Command(sys.executable)(code_path)

    assert result == "b\n"

    code_path.unlink()


def test_dotenv_values_file(dotenv_file: str) -> None:
    """Test ``values`` function."""

    with open(dotenv_file, "w") as env_file:
        env_file.write("a=b")

    result = dotenv.values(dotenv_file)

    assert result == {"a": "b"}


def test_dotenv_values_file_stream(dotenv_file: str) -> None:
    """Test ``dotenv_values`` function."""

    with open(dotenv_file, "w") as env_file:
        env_file.write("a=b")

    with open(dotenv_file, "r") as env_file:
        result = dotenv.values(stream=env_file)

    assert result == {"a": "b"}


@pytest.mark.parametrize(
    argnames=("env", "string", "interpolate", "expected"),
    argvalues=[
        ({"b": "c"}, "a=$b", False, {"a": "$b"}),
        ({"b": "c"}, "a=$b", True, {"a": "$b"}),
        ({"b": "c"}, "a=${b}", False, {"a": "${b}"}),
        ({"b": "c"}, "a=${b}", True, {"a": "c"}),
        ({"b": "c"}, "a=${b:-d}", False, {"a": "${b:-d}"}),
        ({"b": "c"}, "a=${b:-d}", True, {"a": "c"}),
        ({}, "b=c\na=${b}", True, {"a": "c", "b": "c"}),
        ({}, "a=${b}", True, {"a": ""}),
        ({}, "a=${b:-d}", True, {"a": "d"}),
        ({"b": "c"}, 'a="${b}"', True, {"a": "c"}),
        ({"b": "c"}, "a='${b}'", True, {"a": "c"}),
        ({"b": "c"}, "a=x${b}y", True, {"a": "xcy"}),
        ({"a": "b"}, "a=${a}", True, {"a": "b"}),
        ({}, "a=${a}", True, {"a": ""}),
        ({"a": "b"}, "a=${a:-c}", True, {"a": "b"}),
        ({}, "a=${a:-c}", True, {"a": "c"}),
        ({"b": "c"}, "a=${b}${b}", True, {"a": "cc"}),
        ({"b": "c"}, "b=d\na=${b}", True, {"a": "d", "b": "d"}),
        ({}, "a=b\na=c\nd=${a}", True, {"a": "c", "d": "c"}),
        ({}, "a=b\nc=${a}\nd=e\nc=${d}", True, {"a": "b", "c": "e", "d": "e"}),
    ],
)
def test_dotenv_values_string_io(
    env: Dict[str, str],
    string: str,
    interpolate: bool,
    expected: Dict[str, str],
) -> None:
    """Test ``values`` function."""

    with mock.patch.dict(os.environ, env, clear=True):
        stream = io.StringIO(string)
        stream.seek(0)

        result = dotenv.values(stream=stream, interpolate=interpolate)

        assert result == expected
