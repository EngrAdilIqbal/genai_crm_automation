# agents/hubspot_agent.py

from langchain_community.chat_models import ChatOpenAI
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from tools.crm_tools import create_contact_tool, update_contact_tool, create_deal_tool
from langchain_core.utils.function_calling import convert_to_openai_function

llm = ChatOpenAI(model="gpt-4o")

hubspot_tools = [
    create_contact_tool,
    update_contact_tool,
    create_deal_tool
]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful CRM agent."),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

hubspot_agent = create_openai_functions_agent(
    llm=llm,
    tools=[convert_to_openai_function(t) for t in hubspot_tools],
    prompt=prompt
)

hubspot_executor = AgentExecutor(agent=hubspot_agent, tools=hubspot_tools, verbose=True)
