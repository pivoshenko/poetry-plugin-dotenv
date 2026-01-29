"""Module that contains plugin definition."""

from __future__ import annotations

import typing
import pathlib

from cleo.events.console_events import COMMAND
from poetry.plugins.application_plugin import ApplicationPlugin

from poetry_plugin_dotenv import commands
from poetry_plugin_dotenv import configurator
from poetry_plugin_dotenv import loader
from poetry_plugin_dotenv import logging


if typing.TYPE_CHECKING:  # pragma: no cover
    from cleo.events.console_command_event import ConsoleCommandEvent
    from poetry.console.application import Application


COMMANDS_EXCLUSION = {"activate"}


class DotenvPlugin(ApplicationPlugin):
    """Plugin that automatically loads environment variables from a dotenv file."""

    def activate(self, application: Application) -> None:  # pragma: no cover
        application.event_dispatcher.add_listener(  # type: ignore[union-attr]
            event_name=COMMAND,
            listener=self.load,  # type: ignore[arg-type]
        )
        application.command_loader.register_factory("activate", commands.activate_command_factory)

    def load(self, event: ConsoleCommandEvent, *args, **kwargs) -> None:
        command = event.command

        if command.name in COMMANDS_EXCLUSION:
            return  # pragma: no cover

        directory_option = event.io.input.option("directory")
        working_dir = pathlib.Path(directory_option) if directory_option else pathlib.Path.cwd()

        logger = logging.Logger(event)
        config = configurator.Config(working_dir)

        loader.load(
            logger=logger,
            config=config,
            working_dir=working_dir,
        )
