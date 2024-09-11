import operator
from typing import *

# LangChain
from langchain.tools import BaseTool
from langchain_core.messages import AnyMessage, HumanMessage
from langchain_openai import ChatOpenAI

# LangGraph
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

# Tilores
from tilores import TiloresAPI
from langchain_tilores import TiloresTools

# Chainlit
import chainlit as cl
from chainlit.sync import run_sync


class HumanInputChainlit(BaseTool):
    """Tool that adds the capability to ask user for input."""

    name = "human"
    description = (
        "You can ask a human for guidance when you think you "
        "got stuck or you are not sure what to do next. "
        "The input should be a question for the human."
    )

    def _run(self, query: str, run_manager=None) -> str:
        """Use the Human input tool."""

        res = run_sync(cl.AskUserMessage(content=query).send())
        return res["content"]

    async def _arun(self, query: str, run_manager=None) -> str:
        """Use the Human input tool."""
        res = await cl.AskUserMessage(content=query).send()
        return res["output"]


class ChatState(TypedDict):
    messages: Annotated[Sequence[AnyMessage], operator.add]


@cl.on_chat_start
def start():
    llm = ChatOpenAI(temperature=0, streaming=True, model_name="gpt-4o")
    # Setup a connection to the Tilores instance and provide it as a tool
    tilores = TiloresAPI.from_environ()
    tilores_tools = TiloresTools(tilores)
    tools = [
        HumanInputChainlit(),
        tilores_tools.search_tool,
    ]
    # Use MemorySaver to use the full conversation
    memory = MemorySaver()
    state = ChatState(messages=[])
    # Use a LangGraph agent
    agent = create_react_agent(llm, tools, checkpointer=memory)

    # Provide the runnable and state to the user session
    cl.user_session.set("runnable", agent)
    cl.user_session.set("state", state)


@cl.on_message
async def main(message: cl.Message):
    # Retrieve the runnable and state from the user session
    runnable = cl.user_session.get("runnable")
    state = cl.user_session.get("state")

    # Append the new message to the state
    state['messages'] += [HumanMessage(content=message.content)]

    # Stream the response to the UI
    ui_message = cl.Message(content="")
    await ui_message.send()
    async for event in runnable.astream_events(state, version="v1", config={'configurable': {'thread_id': 'thread-1'}}):
        if event["event"] == "on_chat_model_stream":
            content = event["data"]["chunk"].content or ""
            await ui_message.stream_token(token=content)
    await ui_message.update()

