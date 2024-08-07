# Information
This Discord bot is **SERVERLESS** which means it can run for **FREE** and be **ALWAYS online** on [Deta Space](https://deta.space)!  
You can also treat this repository as a template for making serverless bots with the [discohook](https://github.com/jnsougata/discohook) library.

### Table of Contents
- [Information](#information)
- [Table of Contents](#table-of-contents)
- [Features](#features)
- [File Structure](#file-structure)
- [Requirements](#requirements)
- [Running Online](#running-online)
- [Running Locally](#running-locally)
- [Links and Resources](#links-and-resources)

## Features
- `/ping` - a simple command that tells you the bot's latency.
- `/ask <prompt> [model]` - a command that uses [OpenAI's API](https://openai.com/blog/openai-api) (ChatGPT).
- A status message `Listening to /ask! | OpenAI` via [scheduled actions](https://deta.space/docs/en/basics/micros#scheduled-actions).
- And you can easily create and add more commands yourself!

## File Structure
```
.
├─ src/                       # Source code
│  ├─ actions/                # Files used for scheduled actions
│  │  └─ presence.py          # Presence updater (bot status)
│  ├─ assets/                 # All asset files
│  │  └─ logo.png             # Logo used for space app
│  ├─ commands/               # All command files
│  │  ├─ ask.py               # Ask command
│  │  └─ ping.py              # Ping command
│  ├─ utils/                  # Contains any extra utility files
│  │  └─ helpers.py           # Useful functions
│  └─ bot.py                  # Contains the discohook bot
├─ .gitignore                 # Hides certain files
├─ Discovery.md               # Defines app's space discovery page
├─ LICENSE                    # License
├─ README.md                  # Defines this README page
├─ Spacefile                  # Space app configuration
├─ example.env                # Example of an .env file
├─ main.py                    # Entry point
└─ requirements.txt           # Library dependencies
```

## Requirements
- **Discord Application:** Create an app for **FREE** at [Discord Developer Portal](https://discord.com/developers/applications).
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
1. Install the space app from the [app's discovery page](https://deta.space/discovery/@imp1/chatgpt).  
   Alternatively you could build the space app yourself:
   1. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository.
   2. Install the [Space CLI](https://deta.space/docs/en/basics/cli).
   3. Make sure you're in the project folder: `$cd <folder>`
   4. Create a space app: `$space new`
   5. Push the space app: `$space push`
2. Enter the environment variables (Space App Settings ➔ Configuration).
    - `DISCORD_APPLICATION_ID` - Your discord app's ID.
    - `DISCORD_PUBLIC_KEY` - Your discord app's public key.
    - `DISCORD_BOT_TOKEN` - Your bot's token.
    - `OPENAI_API_KEY` - An API key from OpenAI's API.
    - `SYNC_PASSWORD` - A password you set to sync commands later on.
    - Other environment variables are optional.
3. Set `Interactions Endpoint URL` to `<micro_url>/interactions`.
    - This is located in: `https://discord.com/developers/applications/{application_id}/information`
    - A Micro URL looks like this: `https://chatgpt-1-a1234567.deta.app`
4. Visit `<micro_url>/api/dash` to register the slash commands for the first time.
    - You need to type the value of `SYNC_PASSWORD` you set in your env vars.
5. Run `/ping` to make sure it's working! Enjoy!

## Running Locally
You only need to run the bot locally if you plan to **develop new commands** for the bot.    
This is because `$space push`-ing each time would make development take forever.
1. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository.
2. Install the [Space CLI](https://deta.space/docs/en/basics/cli).
3. Make sure you're in the project folder: `$cd <folder>`
4. Install the library dependencies.
    1. Make a virtual environment: `$python -m venv venv`
    2. Enter the virtual environment: `$source venv/bin/activate`
    3. Install requirements: `$pip install -r requirements.txt`
    4. To leave the virtual environment later run `$deactivate`. 
5. Rename `example.env` to `.env` file and update its contents.
    - Environment variables in comments are optional.
6. Run `$space dev` to start both `main` and `bot` micros.
7. In another terminal, start a reverse proxy/tunnel because your `https://localhost` can't be accessed by Discord.  
    - **Via [Deta Space](https://deta.space)**: 
        - Run `space reverse proxy` and the URL is your micro's URL: `https://<name>-1-a1234567.deta.app`
        - If you have a main bot and a test bot, use `space link` to switch to a test space app.
    - **Via [Ngrok](https://ngrok.com)**:
        - [Setup Ngrok](https://ngrok.com/docs/getting-started). Create an account, install CLI, set auth-token.
        - Run `ngrok http 4200` to get a URL like `https://a1b2-34-567-890-123.ngrok-free.app`.
        - Note the Free Tier has a ratelimit of 60 requests per minute and URLs are ephemeral.
     - **Via [Cloudflare](https://cloudflare.com)**:
        - [Setup Cloudflare](https://developers.cloudflare.com/pages/how-to/preview-with-cloudflare-tunnel). Install CLI and optionally link an account.
        - Run `cloudflared tunnel --url https://localhost:4200` to get a URL like `https://ab-quick-brown-fox.trycloudflare.com`.
        - No request ratelimit (AFAIK) but URLs are still ephemeral.
        - Note it's technically against their ToS to host anything other than basic HTML pages on the free plan. 
        - Use this for development only if you need a higher request ratelimit.
     - **List of [other solutions](https://github.com/anderspitman/awesome-tunneling)**.
     - For all the above, you can do `CTRL+C` to stop them.
8. Set the  `Interactions Endpoint URL` to `<url>/interactions`.
    - This is located in: `https://discord.com/developers/applications/{application_id}/information`
    - The URL is from the previous step, for space it's this: `https://<name>-1-a1234567.deta.app`
9. Finally you can now start live editing.  
   Uvicorn is set to `--reload` so any edits you make automatically restarts the webserver.
10. To stop running do `CTRL+C`.

When you're ready, you can run `$space push` to update the space app.

## Links and Resources
- **Deta Space Documentation:** https://deta.space/docs
- **Deta Discord:** https://discord.gg/deta
- **Discohook Discord:** https://discord.gg/xEEpJvE9py
- **Discord API Documentation:** https://discord.com/developers/docs
- **OpenAI API Documenation:** https://platform.openai.com/docs/api-reference?lang=python
- **Space App Discovery Page:** https://deta.space/discovery/@imp1/chatgpt
