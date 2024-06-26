"""Package for the dotenv functionality.

This package is a fork of the ``python-dotenv`` package.

References
----------
#. `python-dotenv <https://github.com/theskumar/python-dotenv>`_

"""

from __future__ import annotations

from poetry_plugin_dotenv.dotenv import core
from poetry_plugin_dotenv.dotenv import parsers
from poetry_plugin_dotenv.dotenv import variables


__all__ = ["core", "parsers", "variables"]
