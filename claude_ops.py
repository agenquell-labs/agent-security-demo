"""Ops agent built with the Claude Agent SDK. INTENTIONALLY INSECURE FIXTURE (AQ09-004)."""
from claude_agent_sdk import ClaudeAgentOptions, query

options = ClaudeAgentOptions(
    system_prompt="You maintain the build server.",
    allowed_tools=["Read", "Bash"],
    permission_mode="bypassPermissions",
)


async def main() -> None:
    async for message in query(prompt="Clean up the build directory", options=options):
        print(message)
