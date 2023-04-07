"""Tests for the module ``src/poetry_plugin_dotenv/plugin.py``."""

from __future__ import annotations

import os

from collections.abc import Callable
from unittest import mock

import pytest
import pytest_mock

from poetry.console.commands.env_command import EnvCommand

from poetry_plugin_dotenv.plugin import DotenvPlugin


@mock.patch.dict(os.environ, {"POETRY_DOTENV_LOCATION": ".env.dev"}, clear=True)
def test_dev_dotenv_file(
    mocker: pytest_mock.MockerFixture,
    create_dotenv_file: Callable[[str, str], dict[str, str]],
    remove_dotenv_file: Callable[[str], None],
) -> None:
    """Test for the ``load`` method."""

    event = mocker.MagicMock()
    event.command = EnvCommand()

    expected_vars = create_dotenv_file("root", ".env.dev")

    plugin = DotenvPlugin()
    plugin.load(event)

    remove_dotenv_file(".env.dev")

    assert expected_vars["POSTGRES_USER"] == os.environ["POSTGRES_USER"]


def test_default_dotenv_file(
    mocker: pytest_mock.MockerFixture,
    create_dotenv_file: Callable[[str, str], dict[str, str]],
    remove_dotenv_file: Callable[[str], None],
) -> None:
    """Test for the ``load`` method."""

    event = mocker.MagicMock()
    event.command = EnvCommand()

    expected_vars = create_dotenv_file("admin", ".env")

    plugin = DotenvPlugin()
    plugin.load(event)

    remove_dotenv_file(".env")

    assert expected_vars["POSTGRES_USER"] == os.environ["POSTGRES_USER"]


@mock.patch.dict(os.environ, {"POETRY_DONT_LOAD_DOTENV": "1"}, clear=True)
def test_without_dotenv_file(
    mocker: pytest_mock.MockerFixture,
    create_dotenv_file: Callable[[str, str], dict[str, str]],
    remove_dotenv_file: Callable[[str], None],
) -> None:
    """Test for the ``load`` method."""

    event = mocker.MagicMock()
    event.command = EnvCommand()

    create_dotenv_file("admin", ".env")

    plugin = DotenvPlugin()
    plugin.load(event)

    remove_dotenv_file(".env")

    # WPS428 - "empty call" is necessary to check the exception
    with pytest.raises(KeyError):
        # noinspection PyStatementEffect
        os.environ["POSTGRES_USER"]  # noqa: WPS428


def test_dotenv_file_doesnt_exist(
    mocker: pytest_mock.MockerFixture,
    remove_dotenv_file: Callable[[str], None],
) -> None:
    """Test for the ``load`` method."""

    event = mocker.MagicMock()
    event.command = EnvCommand()

    remove_dotenv_file(".env")

    plugin = DotenvPlugin()
    plugin.load(event)
