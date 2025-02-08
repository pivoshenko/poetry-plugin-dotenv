"""Module that contains custom exceptions that are used across plugin."""

from __future__ import annotations


class PoetryPluginDotenvError(Exception):
    """Base exception."""


class PoetryPluginDotenvPatternError(PoetryPluginDotenvError):
    """Exception raised when a dotenv pattern is not valid or not found."""
