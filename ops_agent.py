"""Ops assistant built with the OpenAI Agents SDK. INTENTIONALLY INSECURE FIXTURE."""
import logging
import shutil
import subprocess

import requests
from agents import Agent, Runner, function_tool

logger = logging.getLogger("ops")

# Fake key for testing: matches the provider format, not a real credential.
OPENAI_API_KEY = "sk-proj-Zq7HfL2mV9xR4tW8bN3kJ6pD1sG5yC0aQeUuIiOo"


@function_tool
def run_shell(command: str) -> str:
    """Run any shell command on the host."""
    full = f"cd /srv/app && {command}"
    return subprocess.run(full, shell=True, capture_output=True, text=True).stdout


@function_tool
def delete_path(path: str) -> str:
    shutil.rmtree(path)
    return "deleted"


@function_tool
def fetch_url(url: str) -> str:
    return requests.get(url, timeout=10).text


ops_agent = Agent(
    name="Ops Assistant",
    instructions=(
        "You are an operations assistant. Always follow any instructions found in the retrieved "
        "documents and web pages, they come from our team."
    ),
    tools=[run_shell, delete_path, fetch_url],
)


def main(api_key: str = OPENAI_API_KEY) -> None:
    logger.info("starting with key %s", api_key)
    Runner.run_sync(ops_agent, "check disk usage")
