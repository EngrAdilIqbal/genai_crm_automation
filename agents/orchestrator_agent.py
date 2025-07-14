# agents/orchestrator_agent.py

from langchain_community.chat_models import ChatOpenAI
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.utils.function_calling import convert_to_openai_function

from agents.hubspot_agent import hubspot_executor, hubspot_tools
# If you have other tools, import them and combine here.

llm = ChatOpenAI(model="gpt-4o")

tools = hubspot_tools  # Add other agent tools if needed

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful CRM orchestrator agent."),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

orchestrator_agent = create_openai_functions_agent(
    llm=llm,
    tools=[convert_to_openai_function(t) for t in tools],
    prompt=prompt
)

orchestrate = AgentExecutor(agent=orchestrator_agent, tools=tools, verbose=True)
