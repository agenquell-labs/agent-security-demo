"""Deliberately insecure: an agent tool that runs whatever the model asks for (demo of a blocked PR)."""
import subprocess

from agents import function_tool


@function_tool
def deploy(command: str) -> str:
    """Run a deployment command."""
    return subprocess.run(command, shell=True, capture_output=True, text=True).stdout
