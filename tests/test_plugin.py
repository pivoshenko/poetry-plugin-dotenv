"""Tests for the module ``src/poetry_plugin_dotenv/plugin.py``."""

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
    mocker: pytest_mock.MockerFixture,
    create_dotenv_file: Callable[[str, str], dict[str, str]],
    remove_dotenv_file: Callable[[str], None],
) -> None:
    """Test for the ``load`` method."""

    event = mocker.MagicMock()
    event.command = EnvCommand()
    event.io.input.option.return_value = {}

    expected_vars = create_dotenv_file("root", ".env.dev")

    plugin = DotenvPlugin()
    plugin.load(event)

    remove_dotenv_file(".env.dev")

    assert expected_vars["POSTGRES_USER"] == os.environ["POSTGRES_USER"]


@mock.patch(
    "tomlkit.load",
    return_value={
        "tool": {
            "poetry": {
                "plugins": {
                    "dotenv": {
                        "location": ".env.dev",
                    },
                },
            },
        },
    },
)
def test_dev_dotenv_file_toml_config(
    mocker: pytest_mock.MockerFixture,
    create_dotenv_file: Callable[[str, str], dict[str, str]],
    remove_dotenv_file: Callable[[str], None],
) -> None:
    """Test for the ``load`` method."""

    event = mocker.MagicMock()
    event.command = EnvCommand()
    event.io.input.option.return_value = {}

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


@mock.patch.dict(os.environ, {"POETRY_PLUGIN_DOTENV_IGNORE": "y"}, clear=True)
def test_without_dotenv_file_os_config(
    mocker: pytest_mock.MockerFixture,
    create_dotenv_file: Callable[[str, str], dict[str, str]],
    remove_dotenv_file: Callable[[str], None],
) -> None:
    """Test for the ``load`` method."""

    event = mocker.MagicMock()
    event.command = EnvCommand()
    event.io.input.option.return_value = {}

    create_dotenv_file("admin", ".env")

    plugin = DotenvPlugin()
    plugin.load(event)

    remove_dotenv_file(".env")

    with pytest.raises(KeyError):
        os.environ["POSTGRES_USER"]


@mock.patch.dict(os.environ, {}, clear=True)
@mock.patch(
    "tomlkit.load",
    return_value={
        "tool": {
            "poetry": {
                "plugins": {
                    "dotenv": {
                        "ignore": True,
                    },
                },
            },
        },
    },
)
def test_without_dotenv_file_toml_config(
    mocker: pytest_mock.MockerFixture,
    create_dotenv_file: Callable[[str, str], dict[str, str]],
    remove_dotenv_file: Callable[[str], None],
) -> None:
    """Test for the ``load`` method."""

    event = mocker.MagicMock()
    event.command = EnvCommand()
    event.io.input.option.return_value = {}

    create_dotenv_file("admin", ".env")

    plugin = DotenvPlugin()
    plugin.load(event)

    remove_dotenv_file(".env")

    with pytest.raises(KeyError):
        os.environ["POSTGRES_USER"]


def test_dotenv_file_doesnt_exist(
    mocker: pytest_mock.MockerFixture,
    remove_dotenv_file: Callable[[str], None],
) -> None:
    """Test for the ``load`` method."""

    event = mocker.MagicMock()
    event.command = EnvCommand()
    event.io.input.option.return_value = {}

    remove_dotenv_file(".env")

    plugin = DotenvPlugin()
    plugin.load(event)
