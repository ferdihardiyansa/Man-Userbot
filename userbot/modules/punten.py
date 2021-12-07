from time import sleep

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, bot
from userbot.events import man_cmd


@bot.on(man_cmd(outgoing=True, pattern=r"sadboy(?: |$)(.*)"))
async def _(event):
    await event.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await event.edit("`Kedua kamu manis`")
    sleep(1)
    await event.edit("`Dan yang terakhir adalah kamu bukan jodohku`")


# Create by myself @localheart


@bot.on(man_cmd(outgoing=True, pattern=r"badut(?: |$)(.*)"))
async def _(event):
    await event.edit("**Tadi saya beli obat tidur**")
    sleep(3)
    await event.edit("**Pas dibawa pulang harus pelan-pelan**")
    sleep(3)
    await event.edit("**soalnya takut obatnya bangun jiakhhh**")


@bot.on(man_cmd(outgoing=True, pattern=r"maaf(?: |$)(.*)"))
async def _(event):
    await event.edit("**YAUDAH SAYA MINTA MAAF**")
    sleep(3)
    await event.edit("**TAPI BOOONG**")
    sleep(2)
    await event.edit("**BERCANDA XIXIXIXI**")
    

# Create by myself @localheart


CMD_HELP.update(
    {
        "punten": f"**Plugin : **`Animasi Punten`\
        \n\n  •  **Syntax :** `{cmd}maaf` ; `{cmd}badut`\
        \n  •  **Function : **minta maaf\
        \n\n  •  **Syntax :** `{cmd}sadboy`\
        \n  •  **Function : **ya sadboy coba aja.\
    "
    }
)
