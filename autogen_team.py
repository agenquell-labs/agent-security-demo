"""AutoGen team. INTENTIONALLY INSECURE FIXTURE."""
from autogen import AssistantAgent, UserProxyAgent

assistant = AssistantAgent(name="coder", llm_config={"model": "gpt-4o"})
executor = UserProxyAgent(
    name="executor",
    human_input_mode="NEVER",
    code_execution_config={"work_dir": "runs", "use_docker": False},
)
