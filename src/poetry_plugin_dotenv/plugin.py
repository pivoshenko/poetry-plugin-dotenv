"""Module that contains the core functionality of the plugin."""

from __future__ import annotations

import os

from typing import TYPE_CHECKING

from cleo.events.console_events import COMMAND
from poetry.console.commands.env_command import EnvCommand
from poetry.plugins.application_plugin import ApplicationPlugin

from poetry_plugin_dotenv import dotenv
from poetry_plugin_dotenv.config import Config
from poetry_plugin_dotenv.logger import Logger


if TYPE_CHECKING:  # pragma: no cover
    from cleo.events.console_command_event import ConsoleCommandEvent
    from poetry.console.application import Application


class DotenvPlugin(ApplicationPlugin):
    """Plugin that automatically loads environment variables from a dotenv file.

    Plugin that automatically loads environment variables from a dotenv file into the environment
    before ``poetry`` commands are run.
    """

    def activate(self, application: Application) -> None:  # pragma: no cover
        """Activate the plugin."""

        application.event_dispatcher.add_listener(COMMAND, listener=self.load)  # type: ignore[union-attr, arg-type]

    def load(self, event: ConsoleCommandEvent, *args, **kwargs) -> None:  # type: ignore[no-untyped-def]
        """Load a dotenv file based on the provided configuration."""

        working_dir = event.io.input.option("directory") or os.path.curdir

        logger = Logger(event)
        config = Config(working_dir)

        if not isinstance(event.command, EnvCommand):
            return  # pragma: nocover

        if config.ignore:
            logger.warning("Not loading environment variables.")
            return

        filepath = self._determine_filepath(config, working_dir)

        if os.path.isfile(filepath):
            logger.info(f"Loading environment variables from '{filepath}'.")
            dotenv.core.load(filepath)

        else:
            logger.error(f"File '{filepath}' doesn't exist.")

    def _determine_filepath(self, config: Config, working_dir: str) -> str:
        """Determine the appropriate filepath for the dotenv file."""

        if config.location:
            return (
                os.path.abspath(config.location)
                if os.path.isabs(config.location)
                else os.path.join(working_dir, config.location)
            )

        return dotenv.core.find(usecwd=True)
