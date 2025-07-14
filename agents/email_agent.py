# agents/email_agent.py

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain.agents import create_openai_functions_agent, AgentExecutor

from tools.email_tools import send_email_tool

# Initialize your LLM
llm = ChatOpenAI(model="gpt-4o")

# Only include the tools you have
email_tools = [send_email_tool]

# Create the prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful CRM email assistant."),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

# Create the agent
email_agent = create_openai_functions_agent(
    llm=llm,
    prompt=prompt,
    tools=email_tools
)

# Create the executor
email_executor = AgentExecutor(agent=email_agent, tools=email_tools, verbose=True)
