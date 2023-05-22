---
app_name: "ChatGPT"
title: "Serverless ChatGPT Discord Bot"
tagline: "Your personal ChatGPT Discord bot."
theme_color: "#74aa9c"
git: "https://github.com/imptype/serverless-chatgpt-discord-bot"
homepage: "https://deta.space"
---

With this, you can run your own instance of a ChatGPT Discord bot.

### Installation steps:
1. First install the app.
2. Enter the required environment variables:
  - `DISCORD_APPLICATION_ID` - Your discord app's ID.
  - `DISCORD_PUBLIC_KEY` - Your discord app's public key.
  - `DISCORD_BOT_TOKEN` - Your bot's token.
  - `OPENAI_API_KEY` - An API key from OpenAI's API.
3. You can overwrite `CHATGPT_SYSTEM_MESSAGE` to anything you want to transform ChatGPT's personality.
4. Set the `Interactions Endpoint URL` in your discord app's general information to `<micro_url>/bot/interactions`.
5. Visit `<micro_url>/bot/api/dash/<token>` to register the slash commands for the first time.

Run `/ping` to make sure it's working! Enjoy!
