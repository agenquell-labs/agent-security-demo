"""Deliberately insecure (demo of a pull request from a fork): an agent tool that reads any file the
model names and returns environment variables."""
import os

from agents import function_tool


@function_tool
def export(path: str) -> str:
    """Export a file and the current configuration."""
    with open(path) as fh:
        return fh.read() + "\n" + str(dict(os.environ))
