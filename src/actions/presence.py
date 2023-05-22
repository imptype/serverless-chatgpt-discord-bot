import os
import datetime
import logging
import asyncio
import deta # https://github.com/jnsougata/deta
import discohook # https://github.com/jnsougata/discohook

activity_name = '/ask! | OpenAI'
activity_type = 2 # listening to, https://discord.com/developers/docs/topics/gateway-events#activity-object
status = 'online'

token = os.getenv('DISCORD_BOT_TOKEN')
webhook_url = os.getenv('PRESENCE_LOG_WEBHOOK_URL')
deta_project_key = os.getenv('ALT_DETA_PROJECT_KEY', os.getenv('DETA_PROJECT_KEY'))
deta_base_name = 'presence_base'
deta_base_key = 'resume'
deta_base_value = 'value'
gateway_url = 'wss://gateway.discord.gg'
loop_timeout = 20 # max time for scheduled action

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
  '[%(asctime)s.%(msecs)03d] %(message)s', 
  '%Y-%m-%d %H:%M:%S'
))
logger.addHandler(handler)
logger.setLevel(logging.INFO) # set to DEBUG to debug

presence_payload = {
  'activities' : [{
    'name': activity_name,
    'type': activity_type
  }],
  'status' : status,
  'since' : 0,
  'afk' : False
}

async def identify(ws):
  await ws.send_json({
    'op' : 2,
    'd' : {
      'token' : token,
      'intents' : 0, # recieve no events
      'properties' : {
        'os' : 'linux',
        'browser' : 'disco',
        'device' : 'disco'
      },
      'presence' : presence_payload
    }
  })

async def presence_update(ws):
  await ws.send_json({
    'op' : 3,
    'd' : presence_payload
  })

async def resume(ws, session_id, s):
  await ws.send_json({
    'op' : 6,
    'd' : {
      'token' : token,
      'session_id' : session_id,
      'seq' : s
    }
  })

# Resume data stored in 1 record in deta base, looks like this
# key = resume | value = {'url' : 'ws://etc.', 'session_id' : 'asdasd', 's' : s} or record does not exist

async def run(session):
  logger.debug('Enter function')
  task = asyncio.create_task(loop(session))
  try:
    await asyncio.wait_for(task, timeout = loop_timeout + 1)
  except asyncio.TimeoutError: # for local testing, prevents accidental infinite loop
    logger.info('Timed out!')

async def loop(session):
  assert deta_project_key, 'Deta project key not found, give the variable a value if you\'re running this locally.'
  base = deta.Deta(deta_project_key, session = session).base(deta_base_name)
  try:
    data = (await base.get(deta_base_key))[deta_base_value]
    url = data['url']
  except deta.NotFound: # will not exist for first time
    data = None
    url = gateway_url
  while True:
    logger.debug('Connecting to URL: {}'.format(url))
    ws = await session.ws_connect(url)
    async for msg in ws:
      msg = msg.json()

      if msg['op'] == 0: # Dispatch
        
        if msg['t'] == 'READY': # contains guild count, save it somewhere to use
          logger.debug('Ready')
          data = {
            'url' : msg['d']['resume_gateway_url'],
            'session_id' : msg['d']['session_id']
          }
          # count = len(msg['d']['guilds'])

        elif msg['t'] == 'RESUMED':
          logger.debug('Resumed + send PRESENCE UPDATE')
          await presence_update(ws)

        data['s'] = msg['s']
        record = deta.Record({deta_base_value : data}, key = deta_base_key)
        await base.put(record) # updates resume data
        continue

      elif msg['op'] == 9: # Invalid session
        logger.debug('Invalid session, reconnect: {}'.format(msg['d']))
        if not msg['d']: # cant reconnect bool
          await base.delete(deta_base_key) # deletes resume data
          data = None
          url = gateway_url
        await ws.close()
        continue
      
      elif msg['op'] == 10: # Hello
        if data:
          logger.debug('Send RESUME')
          await resume(ws, data['session_id'], data['s'])
          content = 'Resume'
        else:
          logger.debug('Send IDENTIFY')
          await identify(ws)
          content = 'Identify <------ !!'
        content = '[`{}`] {}'.format(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], content)
        if webhook_url:
          await session.post(webhook_url, json = {'content' : content})
        continue

      logger.warning('Unhandled message: {}'.format(msg))
    await asyncio.sleep(1)
