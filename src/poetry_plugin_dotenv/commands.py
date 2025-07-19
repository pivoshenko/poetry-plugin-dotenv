"""Module that contains custom commands."""

from __future__ import annotations

import os
import typing
import pathlib

from poetry.console.commands.env_command import EnvCommand

from poetry_plugin_dotenv import configurator
from poetry_plugin_dotenv import loader
from poetry_plugin_dotenv import logging


if typing.TYPE_CHECKING:  # pragma: no cover
    from poetry.utils.env import Env


def activate_command_factory() -> ActivateCommand:  # pragma: no cover
    return ActivateCommand()


class ActivateCommand(EnvCommand):
    """Command that loads dotenv variables and activates the virtual environment."""

    name = "activate"
    description = (
        "Load environment variables from dotenv file and activate the virtual environment."
    )

    def handle(self) -> int:  # pragma: no cover
        directory_option = self.option("directory")
        working_dir = pathlib.Path(directory_option) if directory_option else pathlib.Path.cwd()

        logger = logging.Logger(self)  # type: ignore[arg-type]
        config = configurator.Config(working_dir)

        activation_command = self._get_venv_activation_command(self.env)
        if not activation_command:
            logger.error("Failed to identify the activation command.")
            return 1

        loader.load(logger, config, working_dir)

        shell = os.environ.get("SHELL", "/bin/bash")
        os.execvp(shell, [shell, "-c", f"{activation_command}; exec {shell}"])  # noqa: S606

        return 0

    def _get_venv_activation_command(self, venv: Env) -> str | None:  # pragma: no cover
        shell = os.environ.get("SHELL", "/bin/bash")

        if "fish" in shell:
            activate_script = venv.path / "bin" / "activate.fish"
            if activate_script.exists():
                return f"source {activate_script}"
            return None

        activate_script = venv.path / "bin" / "activate"
        if activate_script.exists():
            return f"source {activate_script}"

        return None
