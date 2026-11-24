"""Data assistant built with the OpenAI Agents SDK. INTENTIONALLY INSECURE FIXTURE (AQ-06)."""
import os
import sqlite3

from agents import Agent, function_tool
from agents.mcp import MCPServerStdio
from langchain_community.agent_toolkits import create_sql_agent

DB = sqlite3.connect("/srv/app/data/customers.db")


@function_tool
def read_document(path: str) -> str:
    """Read any document the user mentions."""
    with open(path) as fh:
        return fh.read()


@function_tool
def show_config(name: str) -> dict:
    """Show the agent's configuration."""
    return {"value": os.getenv(name), "env": dict(os.environ)}


@function_tool
def lookup_customer(customer: str) -> list:
    query = f"SELECT * FROM customers WHERE name = '{customer}'"
    return DB.execute(query).fetchall()


@function_tool
def run_query(sql: str) -> list:
    return DB.execute(sql).fetchall()


crm = MCPServerStdio(name="crm", params={"command": "crm-mcp"}, require_approval="never")

data_agent = Agent(
    name="Data Assistant",
    instructions="Answer questions about customers.",
    tools=[read_document, show_config, lookup_customer, run_query],
    mcp_servers=[crm],
)

sql_agent = create_sql_agent(llm=None, db=None)
