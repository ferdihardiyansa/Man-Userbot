import sys
import os
import asyncio
from telethon import events

@bot.on(admin_cmd(pattern="hexabot (\d+)?"))
async def _(event):
    input_str = int(event.pattern_match.group(1)) or 15
    await edit_delete(event,"`Ok! Finding.....`")
    while True:
        await event.client.send_message(572621020,"/hunt")
        await asyncio.sleep(input_str)
      

@bot.on(events.NewMessage(from_users=[572621020]))
async def _(event):
    if 'A wild Regigigas' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv) 