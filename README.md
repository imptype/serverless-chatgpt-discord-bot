# Information
This Discord bot is **SERVERLESS** which means it can run for **FREE** and be **ALWAYS online** on [Deta Space](https://deta.space)!  
You can also treat this repository as a template for making serverless bots with the [discohook](https://github.com/jnsougata/discohook) library.

## Table of Contents
- [Information](#information)
- [Table of Contents](#table-of-contents)
- [Features](#features)
- [Requirements](#requirements)
- [Running](#running)
  - [Running Locally](#running-locally)
  - [Running Online](#running-online)
- [Links and Resources](#resources)

## Features
- `/ping` - a simple command that tells you the bot's latency.
- `/ask <prompt> [model]` - a command that uses OpenAI's API (ChatGPT).
- A status message `Listening to /ask! | OpenAI` via scheduled actions.
- And you can easily create and add more commands yourself!

## Requirements
- **Discord Application:** Make an app for **FREE** at [Discord Developer Portal](https://discord.com/developers/applications).
- **Deta Space account:** Create an account for **FREE** at [Deta Space](https://deta.space/), username + password.
- **OpenAI API Key:** Create a developer account for **FREE** at [OpenAI](https://platform.openai.com/overview), free $18 in credits.
- [**discohook**](https://github.com/jnsougata/discohook): A github library used to make async serverless Discord bots.
- [**deta**](https://github.com/jnsougata/discohook): A github library used to make async [Deta Space's Base HTTP API](https://deta.space/docs/en/reference/base/HTTP) requests.
  - The database is only used to store the websocket resume data for the status message.
- [**uvicorn**](https://pypi.org/project/uvicorn/): A PyPI library used to run an ASGI webserver.
- [**python-dotenv**](https://pypi.org/project/python-dotenv/): A PyPI library used to help load variables from an `.env` file.
  - This is only used when developing the bot locally.
- [**openai**](https://pypi.org/project/openai/): A PyPI library used to make async [OpenAI API](https://platform.openai.com/docs/api-reference?lang=python) requests.

# --- Everything below is WIP ---

## Running

### Running Online
2 ways
1. install on space app, see `Discovery.md` for now.
2. push yourself

### Running Locally
- for testing purposes
- to build new commands
- faster
- keep main bot up
- consider using `--reload`
- update `.env`

## Resources
- space docs
- discohook, deta support
- discord api docs
- openai docs
