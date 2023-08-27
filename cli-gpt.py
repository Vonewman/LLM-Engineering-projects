from langchain.tools import ShellTool

shell_tool = ShellTool()

from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import AgentType


llm = ChatOpenAI(temperature=0)

shell_tool.description = shell_tool.description + f"args {shell_tool.args}".replace(
    "{", "{{"
).replace("}", "}}")
agent = initialize_agent(
    [shell_tool], llm, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

agent.run(
    "install numpy in my env environment."
)

