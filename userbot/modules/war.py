from time import sleep

from userbot import ALIVE_NAME
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, bot
from userbot.events import man_cmd


@bot.on(man_cmd(outgoing=True, pattern=r"buah(?: |$)(.*)"))
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**BUAH PAPAYA BUAH PISANG ITULAH NAMA NAMA BUAHAN YANG LEMBEKK SAMA KAYA LU LEMBEL UDAH KAYA TAHU DI BEJEK BEJEK TERUS DI LUDAHIN GAYA GAYAAN SOK KERAS PADAHAL LU AMPAS BEGO GADA KEREN KERENNYA LUU BEGITU YANG ADA NTAR LU KENA MENTAL TERUS LU NANGIS KEJER UDAH KEJER UDAH GITU NGADU KE EMA LU MENDING LU SEKARANG CUCI KAKI CUCI MUKA TERUS TIDUR BEDO **",
    )
    await event.delete()
    
    
