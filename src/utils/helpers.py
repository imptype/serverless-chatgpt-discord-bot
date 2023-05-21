import os
import traceback
import datetime

webhook_url = os.getenv('ERROR_LOG_WEBHOOK_URL')
discord_epoch = 1420070400000

def snowflake_time(snowflake_id):
  return ((snowflake_id >> 22) + discord_epoch) / 1000

async def log_error(session, error):
  text = ''.join(traceback.format_exception(type(error), error, error.__traceback__))
  text = '[{}] {}\n{}'.format(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], error, text)
  print(text) # console
  if webhook_url:
    await session.post(webhook_url, json = {'content' : text[:2000]})

def chunks(text, n):
  return [text[i:i+n] for i in range(0, len(text), n)]