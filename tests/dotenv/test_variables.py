"""Tests for the module ``src/poetry_update/dotenv/variables.py``."""

from typing import List
from typing import Union

import pytest

from poetry_dotenv.dotenv import variables


@pytest.mark.parametrize(
    argnames=("value", "expected"),
    argvalues=[
        ("", []),
        ("a", [variables.Literal(value="a")]),
        ("${a}", [variables.Variable(name="a")]),
        ("${a:-b}", [variables.Variable(name="a", default="b")]),
        (
            "${a}${b}",
            [
                variables.Variable(name="a"),
                variables.Variable(name="b"),
            ],
        ),
        (
            "a${b}c${d}e",
            [
                variables.Literal(value="a"),
                variables.Variable(name="b"),
                variables.Literal(value="c"),
                variables.Variable(name="d"),
                variables.Literal(value="e"),
            ],
        ),
    ],
)
def test_parse(value: str, expected: List[Union[variables.Literal, variables.Variable]]) -> None:
    """Test ``parse`` function."""

    parsed_vars = list(variables.parse(value))
    assert parsed_vars == expected
