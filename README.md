# Information
This Discord bot is **SERVERLESS** which means it can run for **FREE** and be **ALWAYS online** on Deta Space!  
You can also treat this repository as a template for making serverless bots with the discohook library.

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
- Deta Space account
- Discord Application
- Open AI key
- `discohook`
- `deta`
- `python-dotenv`
- `uvicorn`
- `openai`

## Running

### Running Locally
- for testing purposes
- to build new commands
- faster
- keep main bot up
- consider using `--reload`
- update `.env`

### Running Online
2 ways
1. install on space app
2. push yourself

## Resources
- space docs
- discohook, deta support
- discord api docs
- openai docs
