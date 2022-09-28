"""Tests for the module that contains models for dotenv variables/literals."""

from typing import List

import pytest

from poetry_dotenv.dotenv.variables import Literal
from poetry_dotenv.dotenv.variables import parse_variables
from poetry_dotenv.dotenv.variables import Variable


@pytest.mark.parametrize(
    argnames=("value", "expected"),
    argvalues=[
        ("", []),
        ("a", [Literal(value="a")]),
        ("${a}", [Variable(name="a", default=None)]),
        ("${a:-b}", [Variable(name="a", default="b")]),
        (
            "${a}${b}",
            [
                Variable(name="a", default=None),
                Variable(name="b", default=None),
            ],
        ),
        (
            "a${b}c${d}e",
            [
                Literal(value="a"),
                Variable(name="b", default=None),
                Literal(value="c"),
                Variable(name="d", default=None),
                Literal(value="e"),
            ],
        ),
    ],
)
def test_parse_variables(value: str, expected: List[Literal]) -> None:
    """Test ``parse_variables`` function."""

    parsed_vars = parse_variables(value)
    assert list(parsed_vars) == expected


def test_repr() -> None:
    """Test ``__repr__`` and ``__str__`` methods."""

    variable = Variable(name="b", default=None)
    literal = Literal(value="e")

    assert repr(variable) == "Variable(name='b', default=None)"
    assert str(literal) == "Literal(value='e')"
