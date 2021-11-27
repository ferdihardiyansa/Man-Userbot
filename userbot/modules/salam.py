from time import sleep

from userbot import ALIVE_NAME
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, bot
from userbot.events import man_cmd


@bot.on(man_cmd(outgoing=True, pattern="p(?: |$)(.*)"))
async def _(event):
    await event.edit("**Assalamualaikum ukhti**")


@bot.on(man_cmd(outgoing=True, pattern="makan(?: |$)(.*)"))
async def _(event):
    await event.edit("**KAMU UDAH MAKAN BELUM**")
    sleep(3)
    await event.edit("**KALAU BELUM MATI AJA SEKALIAN**")
    sleep(3)
    await  event.edit("**BECANDA**")
   

@bot.on(man_cmd(outgoing=True, pattern=r"pe(?: |$)(.*)"))
async def _(event):
    await event.edit("**Assalamualaikum akhi**")


@bot.on(man_cmd(outgoing=True, pattern="jawab(?: |$)(.*)"))
async def _(event):
    await event.edit(f"**Haii Salken Saya {ALIVE_NAME}**")
    sleep(2)
    await event.edit("**wa'laikumsalam ukhti**")


@bot.on(man_cmd(outgoing=True, pattern=r"l(?: |$)(.*)"))
async def _(event):
    await event.edit("**Wa'alaikumsalam**")


@bot.on(man_cmd(outgoing=True, pattern=r"gombalan(?: |$)(.*)"))
async def _(event):
    await event.edit("**IKAN HIU MELAYANG LAYANG**")
    sleep(2)
    await event.edit("**I LOVE YOU SAYANG JIAKHHH**")


@bot.on(man_cmd(outgoing=True, pattern=r"kabar(?: |$)(.*)"))
async def _(event):
    await event.edit(f"** Hallo beb **")
    sleep(2)
    await event.edit("**gimana kabarnya**")


@bot.on(man_cmd(outgoing=True, pattern=r"ass(?: |$)(.*)"))
async def _(event):
    await event.edit("**Salam Dulu Biar Sopan**")
    sleep(2)
    await event.edit("**السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ**")
    
CMD_HELP.update(
    {
        "salam": f"**Plugin : **`salam`\
        \n\n  •  **Syntax :** `{cmd}p`\
        \n  •  **Function : **Assalamualaikum Dulu Biar Sopan..\
        \n\n  •  **Syntax :** `{cmd}pe`\
        \n  •  **Function : **salam Kenal dan salam\
        \n\n  •  **Syntax :** `{cmd}l`\
        \n  •  **Function : **Untuk Menjawab salam\
        \n\n  •  **Syntax :** `{cmd}ass`\
        \n  •  **Function : **Salam Bahas arab\
        \n\n  •  **Syntax :** `{cmd}ywc`\
        \n  •  **Function : **nMenampilkan sama sama syang\
        \n\n  •  **Syntax :** `{cmd}makan`\
        \n  •  **Function : ** `nanyain kabar makan`\
        \n\n  •  **Syntax :** `{cmd}k`\
        \n  •  **Function : **nanyain kabar\
        \n\n  •  **Syntax :** `{cmd}gombalan`\
        \n  •  **Function : **untuk gombalan\
    "
    }
)
