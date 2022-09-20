"""Tests for the plugin."""

import os

from typing import Callable
from typing import Dict
from unittest import mock

import pytest
import pytest_mock

from poetry.console.commands.env_command import EnvCommand

from poetry_dotenv.plugin import DotenvPlugin


@mock.patch.dict(os.environ, {"POETRY_DOTENV_LOCATION": ".env.dev"}, clear=True)
def test_dev_dotenv_file(
    mocker: pytest_mock.MockerFixture,
    crearte_dotenv_file: Callable[[str, str], Dict[str, str]],
) -> None:
    """Test for the plugin with the dev dotenv file location."""

    event = mocker.MagicMock()
    event.command = EnvCommand()

    expected_vars = crearte_dotenv_file(user="root", filename=".env.dev")

    plugin = DotenvPlugin()
    plugin.load_dotenv(event)

    assert expected_vars["POSTGRES_USER"] == os.environ["POSTGRES_USER"]


def test_default_dotenv_file(
    mocker: pytest_mock.MockerFixture,
    crearte_dotenv_file: Callable[[str, str], Dict[str, str]],
) -> None:
    """Test for the plugin with the default dotenv file location."""

    event = mocker.MagicMock()
    event.command = EnvCommand()

    expected_vars = crearte_dotenv_file(user="admin", filename=".env")

    plugin = DotenvPlugin()
    plugin.load_dotenv(event)

    assert expected_vars["POSTGRES_USER"] == os.environ["POSTGRES_USER"]


@mock.patch.dict(os.environ, {"POETRY_DONT_LOAD_DOTENV": "1"}, clear=True)
def test_without_dotenv_file(
    mocker: pytest_mock.MockerFixture,
    crearte_dotenv_file: Callable[[str, str], Dict[str, str]],
) -> None:
    """Test for the plugin without loading the dotenv file."""

    event = mocker.MagicMock()
    event.command = EnvCommand()

    crearte_dotenv_file(user="admin", filename=".env")

    plugin = DotenvPlugin()
    plugin.load_dotenv(event)

    # WPS428 - "empty call" is neccessary to check the exception
    with pytest.raises(KeyError):
        os.environ["POSTGRES_USER"]  # noqa: WPS428
