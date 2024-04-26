"""Tests for the module ``src/poetry_plugin_dotenv/config.py``."""

from __future__ import annotations

import pytest

from poetry_plugin_dotenv.config import _as_bool


@pytest.mark.parametrize(
    argnames=("value", "expected_bool"),
    argvalues=[
        ("y", True),
        ("yes", True),
        ("t", True),
        ("on", True),
        ("1", True),
        ("true", True),
        ("n", False),
        ("no", False),
        ("f", False),
        ("off", False),
        ("0", False),
        ("false", False),
        pytest.param("nope", None, marks=pytest.mark.xfail(raises=ValueError)),
    ],
)
def test__as_bool(value: str, expected_bool: bool) -> None:  # noqa: FBT001
    """Test for the ``_as_bool`` function."""

    assert expected_bool == _as_bool(value)
