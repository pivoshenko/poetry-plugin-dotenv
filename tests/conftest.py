"""Fixtures and configuration for the tests."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import pytest


if TYPE_CHECKING:
    from collections.abc import Callable
    from collections.abc import Iterator


@pytest.fixture
def create_dotenv_file(tmp_path: Path) -> Callable[[dict[str, str], str], None]:
    """Get a dotenv file."""

    def create(content: dict[str, str], filename: str) -> None:
        dotenv_file = tmp_path / ".." / ".." / ".." / filename
        stream = (f"{kay!s}={value!s}" for kay, value in content.items())
        dotenv_file.write_text("/n".join(stream))

    return create


@pytest.fixture
def remove_dotenv_file() -> Callable[[str], None]:
    """Remove a dotenv file."""

    def remove(filepath: str) -> None:
        path = Path(filepath)
        if path.exists():
            path.unlink()

    return remove


@pytest.fixture
def dotenv_file(tmp_path: Path) -> Iterator[str]:
    """Get a dotenv file."""
    filepath = tmp_path / ".env"
    filepath.write_bytes(b"")

    yield str(filepath)
    filepath.unlink()
