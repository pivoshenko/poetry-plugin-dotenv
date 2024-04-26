"""Example script."""  # noqa: INP001

from __future__ import annotations

import os


if __name__ == "__main__":
    try:
        print(f"Host: {os.environ['DB__HOST']!r}")  # noqa: T201
        print(f"Name: {os.environ['DB__DBNAME']!r}")  # noqa: T201
        print(f"Username: {os.environ['DB__USER']!r}")  # noqa: T201
        print(f"Password: {os.environ['DB__PASSWORD']!r}")  # noqa: T201
        print(f"Engine: {os.environ['DB__ENGINE']!r}")  # noqa: T201

    except KeyError:
        print("Environment variables not set!")  # noqa: T201
