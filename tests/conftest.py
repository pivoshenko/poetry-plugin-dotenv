"""Fixtures and configuration for the tests."""

from __future__ import annotations

import os

from typing import TYPE_CHECKING

import pytest


if TYPE_CHECKING:
    from collections.abc import Callable
    from collections.abc import Generator
    from pathlib import Path


@pytest.fixture()
def create_dotenv_file(tmp_path: Path) -> Callable[[str, str], dict[str, str]]:
    """Get a dotenv file."""

    def create(user: str, filename: str) -> dict[str, str]:
        """Create a dotenv file."""

        dotenv_content = {"POSTGRES_USER": user}
        dotenv_file = tmp_path / ".." / ".." / ".." / filename
        stream = (f"{kay!s}={value!s}" for kay, value in dotenv_content.items())
        dotenv_file.write_text("/n".join(stream))

        return dotenv_content

    return create


@pytest.fixture()
def remove_dotenv_file() -> Callable[[str], None]:
    """Remove a dotenv file."""

    def remove(filepath: str) -> None:
        """Remove a dotenv file."""

        if os.path.exists(filepath):
            os.unlink(filepath)

    return remove


@pytest.fixture()
def dotenv_file(tmp_path: Path) -> Generator:
    """Get a dotenv file."""

    filepath = tmp_path / ".env"
    filepath.write_bytes(b"")

    yield str(filepath)
    filepath.unlink()
