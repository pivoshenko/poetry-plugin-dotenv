"""Fixtures and configuration for the tests."""

from pathlib import Path

import pytest


@pytest.fixture()
def dotenv_content() -> str:
    """Get content of the ``.env`` file."""

    return "POSTGRES_USER=admin"


@pytest.fixture()
def dotenv_filepath(dotenv_content: str, tmp_path: Path) -> str:
    """Get ``.env`` filepath."""

    basepath = tmp_path / ".." / ".." / ".."

    filepath = basepath / ".env"
    filepath.write_text(dotenv_content)

    yield filepath

    filepath.unlink()
