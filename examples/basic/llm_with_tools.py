from tilores import TiloresAPI
from langchain_tilores import TiloresTools
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Initialize the Tilores API.
tilores = TiloresAPI.from_environ()
# TiloresTools helps you build typed tools from a specific Tilores instance, typed according to
# the schema of the instance.
tilores_tools = TiloresTools(tilores)

# Setup a LLM model for inference bound with a set of tools.
tools = [tilores_tools.search_tool()]
tools_dict = {tool.name: tool for tool in tools}
model = ChatOpenAI(temperature=0, streaming=True, model_name="gpt-4o")
model = model.bind_tools(tools)

# The basic loop works like this, that a list of messages is passed to the LLM
messages = [
    HumanMessage("Find me an entity by the first name Emma, surname Schulz, born on 1988-03-12")
]
ai_message = model.invoke(messages)
messages.append(ai_message)

# And for each AiMessage, you must check if it wants to invoke tools.
for tool_call in ai_message.tool_calls:
    # Perform the tool call and append the ToolMessage to the list of messages
    selected_tool = tools_dict[tool_call['name']]
    tool_message = selected_tool.invoke(tool_call)
    messages.append(tool_message)

# Then continue the basic loop by invoking the LLM with the current state, passing the list of messages.
ai_response = model.invoke(messages)
print(ai_response.content)

