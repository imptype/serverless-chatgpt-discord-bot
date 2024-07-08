import time
import discohook
from ..utils.helpers import snowflake_time

@discohook.command.slash('ping', description = 'Ping test the bot.')
async def ping_command(interaction):
  created_at = snowflake_time(int(interaction.id))
  now = time.time()
  since = now - created_at
  content = 'Pong! Latency: `{:.2f}ms`'.format(since * 1000)
  await interaction.response.send(content)