# Tilores example of a LLM with tilores_search

This simple Python script demonstrates how to use the Tilores Python SDK with the LangChain ecosystem.

Here we combine:

* LangChain
* Tilores SDK
* LangChain Tilores

To build a comprehensive Human-in-the-Loop chat application for interacting with the
Tilores entity resolution system.

It works and adapts itself automatically to any Tilores instance schema, and works for
any number of tools provided.

## Demo

```console
$ cd examples/basic/
$ pip install -r requirements.txt
$ python llm_with_tools.py
I found multiple records for an entity with the first name Emma, surname Schulz, born on 1988-03-12. Here are the details:

1. **Record ID:** cc001001-0006-4000-c000-000000000006
   - **First Name:** Emma
   - **Last Name:** Schulz
   - **Date of Birth:** 1988-03-12

2. **Record ID:** cc001001-0002-4000-c000-000000000002
   - **First Name:** Emma
   - **Last Name:** Schulz
   - **Date of Birth:** 1988-03-12

[... snip ...]

If you need more specific information or further assistance, please let me know!
```

