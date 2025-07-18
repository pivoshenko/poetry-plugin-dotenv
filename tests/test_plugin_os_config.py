"""Tests for the module that contains plugin definition."""

from __future__ import annotations

import os

from typing import TYPE_CHECKING
from unittest import mock

import pytest

from poetry.console.commands.env_command import EnvCommand

from poetry_plugin_dotenv.plugin import DotenvPlugin


if TYPE_CHECKING:
    from collections.abc import Callable

    import pytest_mock


@mock.patch.dict(os.environ, {"POETRY_PLUGIN_DOTENV_LOCATION": ".env.dev"}, clear=True)
def test_dev_dotenv_file_os_config(
    mocker: pytest_mock.MockFixture,
    create_dotenv_file: Callable[[dict[str, str], str], None],
    remove_dotenv_file: Callable[[str], None],
) -> None:
    event = mocker.MagicMock()
    event.command = EnvCommand()
    event.io.input.option.return_value = None

    filename = ".env.dev"
    content = {"POSTGRES_USER": "root"}

    create_dotenv_file(content, filename)

    plugin = DotenvPlugin()
    plugin.load(event)

    remove_dotenv_file(filename)

    assert content["POSTGRES_USER"] == os.environ["POSTGRES_USER"]


@mock.patch.dict(os.environ, {"POETRY_PLUGIN_DOTENV_IGNORE": "y"}, clear=True)
def test_without_dotenv_file_os_config(
    mocker: pytest_mock.MockFixture,
    create_dotenv_file: Callable[[dict[str, str], str], None],
    remove_dotenv_file: Callable[[str], None],
) -> None:
    event = mocker.MagicMock()
    event.command = EnvCommand()
    event.io.input.option.return_value = None

    filename = ".env"
    content = {"POSTGRES_USER": "admin"}

    create_dotenv_file(content, filename)

    plugin = DotenvPlugin()
    plugin.load(event)

    remove_dotenv_file(filename)

    with pytest.raises(KeyError):
        os.environ["POSTGRES_USER"]
