from dotenv import load_dotenv

# Load env if running locally
load_dotenv(override = True)

import os
import asyncio
import contextlib
import aiohttp
import discohook
from ..commands.ask import ask_command
from ..commands.ping import ping_command
from ..utils.helpers import log_error

# Define the bot
app = discohook.Client(
  application_id = int(os.getenv('DISCORD_APPLICATION_ID')),
  public_key = os.getenv('DISCORD_PUBLIC_KEY'),
  token = os.getenv('DISCORD_BOT_TOKEN')
)

# Lifespan to create and cleanup sessions
@contextlib.asynccontextmanager
async def lifespan(app):
  app.session = aiohttp.ClientSession()
  try:
    yield
  except asyncio.CancelledError as error:
    print('Ignoring cancelled error. (CTRL+C)')
  await app.http.session.close()
  await app.session.close()
app.router.lifespan_context = lifespan

# Error handler
@app.on_error
async def on_error(interaction, error):
  if interaction.responded:
    await interaction.followup('Sorry, an error has occured (after responding).')
  else:
    await interaction.response('Sorry, an error has occured.')
  await log_error(app.session, error)

# Add commands
app.add_commands(
  ask_command,
  ping_command
)