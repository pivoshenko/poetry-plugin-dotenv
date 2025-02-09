"""Example script."""

from __future__ import annotations

import os


if __name__ == "__main__":
    try:
        print(f"Host: {os.environ['DB__HOST']!r}")
        print(f"Name: {os.environ['DB__DBNAME']!r}")
        print(f"Username: {os.environ['DB__USER']!r}")
        print(f"Password: {os.environ['DB__PASSWORD']!r}")
        print(f"Engine: {os.environ['DB__ENGINE']!r}")

    except KeyError:
        print("Environment variables not set!")
