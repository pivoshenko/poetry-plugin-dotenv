"""poetry-plugin-dotenv - is the plugin that automatically loads environment variables from a dotenv file into the environment before poetry commands are run."""

__title__ = "poetry-plugin-dotenv"
__summary__ = "poetry-plugin-dotenv - is the plugin that automatically loads environment variables from a dotenv file into the environment before poetry commands are run."
__uri__ = "https://github.com/pivoshenko/poetry-plugin-dotenv"

__version__ = "2.1.4"

__author__ = "Volodymyr Pivoshenko"
__email__ = "volodymyr.pivoshenko@gmail.com"

__license__ = "MIT"
__copyright__ = "Copyright 2023, Volodymyr Pivoshenko"

from poetry_plugin_dotenv import config
from poetry_plugin_dotenv import dotenv
from poetry_plugin_dotenv import plugin


__all__ = ["dotenv", "plugin", "config"]
