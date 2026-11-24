"""LangChain research agent. INTENTIONALLY INSECURE FIXTURE."""
import shutil

from langchain.globals import set_debug
from langchain_community.tools import ShellTool
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

set_debug(True)

DB_PASSWORD = "Pr0dDbPassw0rd2024x"



@tool
def purge_cache(path: str) -> str:
    """Delete a cache directory."""
    shutil.rmtree(path)
    return "purged"


tools = [ShellTool(), purge_cache]
research_agent = create_react_agent("openai:gpt-4o", tools=tools)
