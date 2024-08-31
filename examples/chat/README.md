# Tilores Human-in-the-Loop

This chat application showcases how to use the Tilores Python SDK within the Python and LangChain ecosystem.

In this setup, we integrate:

* Chainlit
* LangGraph
* LangChain
* Tilores SDK
* LangChain Tilores

The application provides a comprehensive Human-in-the-Loop interface for interacting with the
Tilores entity resolution system.

It automatically adapts to any Tilores instance schema and supports any number of tools.

## Demo

```
$ cd examples/chat/
$ pip install -r requirements.txt
$ chainlit run chat.py -w
```

