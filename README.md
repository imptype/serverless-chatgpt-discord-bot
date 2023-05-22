# Information
This Discord bot is **SERVERLESS** which means it can run for **FREE** and be **ALWAYS online** on [Deta Space](https://deta.space)!  
You can also treat this repository as a template for making serverless bots with the [discohook](https://github.com/jnsougata/discohook) library.

## Table of Contents
- [Information](#information)
- [Table of Contents](#table-of-contents)
- [Features](#features)
- [Requirements](#requirements)
- [Running Online](#running-online)
- [Running Locally](#running-locally)
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

## Running Online
1. Install the space app from the app's discovery page.  
   Alternatively you could build the space app yourself:
   1. Clone this repository.
   2. Install the [Space CLI](https://deta.space/docs/en/basics/cli).
   3. Make sure you're in the project folder: `$cd <folder>`
   4. Create a space app: `$space new`
   5. Push the space app: `$space push`
2. Enter the environment variables (Space App Settings ➔ Configuration).
    - `DISCORD_APPLICATION_ID` - Your discord app's ID.
    - `DISCORD_PUBLIC_KEY` - Your discord app's public key.
    - `DISCORD_BOT_TOKEN` - Your bot's token.
    - `OPENAI_API_KEY` - An API key from OpenAI's API.
    - Other environment variables are optional.
3. Set `Interactions Endpoint URL` to `<micro_url>/bot/interactions`.
    - This is located in: `https://discord.com/developers/applications/{application_id}/information`
    - A Micro URL looks like this: `https://chatgpt-1-a1234567.deta.app/`
4. Visit `<micro_url>/bot/api/dash/<discord_bot_token>` to register the slash commands for the first time.
5. Run `/ping` to make sure it's working! Enjoy!

# --- Everything below is WIP ---

## Running Locally
You may want to run the bot locally when it comes to making new commands otherwise you'd have `space push` each time and that would make development take forever.
1. Clone this repository.
2. Install the [Space CLI](https://deta.space/docs/en/basics/cli).
3. Make sure you're in the project folder: `$cd <folder>`
4. Run `space dev` to run both `main` and `bot` micros.
  1. Do `CTRL+C` to stop running.
5. Set up a reverse proxy to forward local host
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
