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

## Prerequisites
To start the demo, you'll need to input your OpenAI API key and the connection information for a Tilores instance as environment variables. For your convenience, the Tilores connection details for the demo instance have already been pre-filled.

```
export OPENAI_API_KEY='your key'
export TILORES_API_URL='https://8edvhd7rqb.execute-api.eu-central-1.amazonaws.com'
export TILORES_TOKEN_URL='https://saas-umgegwho-tilores.auth.eu-central-1.amazoncognito.com/oauth2/token'
export TILORES_CLIENT_ID='3l3i0ifjurnr58u4lgf0eaeqa3'
export TILORES_CLIENT_SECRET='1c0g3v0u7pf1bvb7v65pauqt6s0h3vkkcf9u232u92ov3lm4aun2'
```

## Demo

The demo can be used with a preconfigured Tilores instance that is already loaded with some sample data.

```
$ cd examples/chat/
$ pip install -r requirements.txt
$ chainlit run chat.py -w
```

## Example Data
```
Firstname: Sophia
Lastname: Muller
Birthdate: 1990-04-15
```
