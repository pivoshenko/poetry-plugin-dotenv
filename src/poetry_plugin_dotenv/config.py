"""Module that contains plugin's configurator."""

from __future__ import annotations

import os
import dataclasses

import tomlkit


CONFIG_SOURCES: dict[str, str] = {
    "pyproject.toml": "tool.poetry.plugins.dotenv",
    "os": "POETRY_PLUGIN_DOTENV_",
}

_STR_BOOLEAN_MAPPING: dict[str, bool] = {
    "y": True,
    "yes": True,
    "t": True,
    "on": True,
    "1": True,
    "true": True,
    "n": False,
    "no": False,
    "f": False,
    "off": False,
    "0": False,
    "false": False,
}


@dataclasses.dataclass
class _Config:
    """Defines the data schema and defaults used for plugin configuration."""

    ignore: bool = False
    location: str = ""


# TODO(pivoshenko): this configuration loader is a "quick patch" solution
class Config(_Config):
    """Configuration loader."""

    def __init__(self, working_dir: str) -> None:
        """Initialize and load configuration from sources."""

        super().__init__()

        source_config = {}
        for config_source, section in CONFIG_SOURCES.items():
            if config_source.endswith(".toml"):
                config = _load_config_from_toml(os.path.join(working_dir, config_source), section)

            elif config_source.endswith("os"):
                config = _load_config_from_os(section)

            else:  # pragma: no cover
                pass

            source_config.update(config)

        self._apply_source_config(source_config)

    def _apply_source_config(self, source_config: dict[str, str | bool | None]) -> None:
        """Apply source configuration to the instance."""

        for field in self.__dataclass_fields__.values():
            source_value = source_config.get(field.name)

            if (
                isinstance(field.default, bool)
                and source_value
                and not isinstance(source_value, bool)
            ):
                source_value = _as_bool(source_value)

            if source_value is not None:
                setattr(self, field.name, source_value)


def _load_config_from_toml(filepath: str, section: str) -> dict[str, str | bool | None]:
    """Load configuration from the TOML file."""

    if not os.path.exists(filepath):
        return {}

    with open(filepath, "rb") as toml_file:
        config = tomlkit.load(toml_file)

    for key in section.split("."):
        config = config.get(key, {})

    return config if isinstance(config, dict) else {}


def _load_config_from_os(section: str) -> dict[str, str | bool | None]:
    """Load configuration from the OS environment variables."""

    return {
        key[len(section) :].lower(): value
        for key, value in os.environ.items()
        if key.startswith(section)
    }


def _as_bool(value: str) -> bool:
    """Convert a string value to a Boolean equivalent.

    Heavily inspired from ``distutils strtobool``.
    """

    try:
        return _STR_BOOLEAN_MAPPING[value.lower()]

    except KeyError:
        msg = f"Invalid truth value '{value}'"
        raise ValueError(msg) from None
