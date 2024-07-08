import os
import asyncio
import contextlib
import aiohttp
import discohook
from starlette.responses import JSONResponse, PlainTextResponse
from .commands.ask import ask_command
from .commands.ping import ping_command
from .actions import presence
from .utils.helpers import log_error

def run():

  # Lifespan to cleanup sessions during development
  @contextlib.asynccontextmanager
  async def lifespan(app):
    async with aiohttp.ClientSession() as app.session:
      try:
        yield
      finally:
        if app.http.session: # close bot session
          await app.http.session.close()

  # Define the bot
  app = discohook.Client(
    application_id = int(os.getenv('DISCORD_APPLICATION_ID')),
    public_key = os.getenv('DISCORD_PUBLIC_KEY'),
    token = os.getenv('DISCORD_BOT_TOKEN'),
    password = os.getenv('SYNC_PASSWORD'),
    lifespan = lifespan
  )

  # Interactions error handler
  @app.on_interaction_error()
  async def on_interaction_error(interaction, error):
    if interaction.responded:
      await interaction.followup('Sorry, an error has occurred (after responding).')
    else:
      await interaction.response('Sorry, an error has occurred.')
    await log_error(app.session, error)

  # Server error handler
  @app.on_error()
  async def on_error(request, error):
    await log_error(app.session, error)
    return JSONResponse({'error' : str(error)})

  # Add commands
  app.add_commands(
    ask_command,
    ping_command
  )

  # Root
  @app.route('/', methods = ['GET'])
  async def root(request):
    return PlainTextResponse('Your micro is online. See the Discovery page to finish setting up!')

  # Actions handler
  @app.route('/__space/v0/actions', methods = ['POST'])
  async def actions(request):
    data = await request.json()
    event = data['event']
    if event['id'] == 'presence':
      await presence.run(app.session)

  return app