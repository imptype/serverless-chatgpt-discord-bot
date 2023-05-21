from dotenv import load_dotenv

# Load env if running locally
load_dotenv(override = True) # '.env' file is not included when deployed to Space

import asyncio
import contextlib
import aiohttp
from fastapi import FastAPI, Request
from fastapi.responses import Response
from ..actions import presence
from ..utils.helpers import log_error

# Lifespan to attach .session attribute, cancel + shutdown is for local testing
@contextlib.asynccontextmanager
async def lifespan(app):
  app.session = aiohttp.ClientSession()
  try:
    yield
  except asyncio.CancelledError:
    print('Ignoring cancelled error. (CTRL+C)')
  await app.session.close()

app = FastAPI(lifespan = lifespan)

# Error handler
@app.middleware('http')
async def middleware(request, call_next):
  try:
    return await call_next(request)
  except Exception as error:
    await log_error(app.session, error)
    return Response('Internal server error', status_code = 500)

# Root
@app.get('/')
async def root():
  return 'There is no app here, this just runs the serverless bot behind-the-scenes. See the Discovery page for setting up!'

# Actions handler
@app.post('/__space/v0/actions')
async def actions(request : Request):
  data = await request.json()
  event = data['event']
  if event['id'] == 'presence':
    await presence.run(app.session)
