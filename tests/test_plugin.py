"""Tests for the module that contains the core functionality of the plugin."""

import os

from typing import Callable
from typing import Dict
from unittest import mock

import pytest
import pytest_mock

from poetry.console.commands.env_command import EnvCommand

from poetry_dotenv.plugin import DotenvPlugin


@mock.patch.dict(os.environ, {"POETRY_DOTENV_LOCATION": ".env.dev"}, clear=True)
def test_load_dotenv_non_default_file(
    mocker: pytest_mock.MockerFixture,
    create_dotenv_file: Callable[[str, str], Dict[str, str]],
    remove_dotenv_file: Callable[[str], None],
) -> None:
    """Test ``load_dotenv`` function with a non default dotenv file."""

    event = mocker.MagicMock()
    event.command = EnvCommand()

    # noinspection PyArgumentList
    expected_vars = create_dotenv_file("root", ".env.dev")

    plugin = DotenvPlugin()
    plugin.load_dotenv(event)

    assert expected_vars["POSTGRES_USER"] == os.environ["POSTGRES_USER"]

    remove_dotenv_file(".env.dev")


def test_load_dotenv_default_file(
    mocker: pytest_mock.MockerFixture,
    create_dotenv_file: Callable[[str, str], Dict[str, str]],
    remove_dotenv_file: Callable[[str], None],
) -> None:
    """Test ``load_dotenv`` function with a default dotenv file."""

    event = mocker.MagicMock()
    event.command = EnvCommand()

    # noinspection PyArgumentList
    expected_vars = create_dotenv_file("admin", ".env")

    plugin = DotenvPlugin()
    plugin.load_dotenv(event)

    assert expected_vars["POSTGRES_USER"] == os.environ["POSTGRES_USER"]

    remove_dotenv_file(".env")


@mock.patch.dict(os.environ, {"POETRY_DONT_LOAD_DOTENV": "1"}, clear=True)
def test_load_dotenv_without_file(
    mocker: pytest_mock.MockerFixture,
    create_dotenv_file: Callable[[str, str], Dict[str, str]],
) -> None:
    """Test ``load_dotenv`` function without a dotenv file."""

    event = mocker.MagicMock()
    event.command = EnvCommand()

    # noinspection PyArgumentList
    create_dotenv_file("admin", ".env")

    plugin = DotenvPlugin()
    plugin.load_dotenv(event)

    # WPS428 - "empty call" is necessary to check the exception
    with pytest.raises(KeyError):
        # noinspection PyStatementEffect
        os.environ["POSTGRES_USER"]  # noqa: WPS428
