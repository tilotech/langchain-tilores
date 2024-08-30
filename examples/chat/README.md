# Tilores Human-in-the-Loop

This chat application provides a demonstration on how to use the Tilores Python SDK
with the Python and LangChain ecosystem.

Here we combine:

* Chainlit
* LangGraph
* LangChain

To build a comprehensive Human-in-the-Loop chat application for interacting with the
Tilores entity resolution system.

It works and adapts itself automatically to any Tilores instance schema, and works for
any number of tools provided.

## Demo

```
$ cd examples/chat/
$ pip install -r requirements.txt
$ chainlit run chat.py -w
```

