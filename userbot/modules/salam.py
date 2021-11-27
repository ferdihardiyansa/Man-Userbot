from time import sleep

from userbot import ALIVE_NAME
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, bot
from userbot.events import man_cmd


@bot.on(man_cmd(outgoing=True, pattern="p(?: |$)(,*)"))
async def _(event):
    await event.edit("**Assalamualaikum Dulu Biar Sopan**")


@bot.on(man_cmd(outgoing=True, pattern=r"pe(?: |$)(,*)"))
async def _(event):
    await event.edit("**Assalamualaikum Warahmatullahi Wabarakatuh**")


@bot.on(man_cmd(outgoing=True, pattern="P(?: |$)(,*)"))
async def _(event):
    await event.edit(f"**Haii Salken Saya {ALIVE_NAME}**")
    sleep(2)
    await event.edit("**Assalamualaikum...**")


@bot.on(man_cmd(outgoing=True, pattern=r"l(?: |$)(,*)"))
async def _(event):
    await event.edit("**Wa'alaikumsalam**")


@bot.on(man_cmd(outgoing=True, pattern=r"a(?: |$)(,*)"))
async def _(event):
    await event.edit(f"**Haii Salken Saya {ALIVE_NAME}**")
    sleep(2)
    await event.edit("**Assalamualaikum**")


@bot.on(man_cmd(outgoing=True, pattern=r"j(?: |$)(,*)"))
async def _(event):
    await event.edit("**IKAN HIU MELAYANG LAYANG**")
    sleep(3)
    await event.edit("**I LOVE YOU SAYANG**")


@bot.on(man_cmd(outgoing=True, pattern=r"k(?: |$)(,*)"))
async def _(event):
    await event.edit(f"** Hallo beb **")
    sleep(2)
    await event.edit("**gimana kabarnya**")


@bot.on(man_cmd(outgoing=True, pattern=r"ass(?: |$)(,*)"))
async def _(event):
    await event.edit("**Salam Dulu Biar Sopan**")
    sleep(2)
    await event.edit("**السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ**")

@bot.on(man_cmd(outgoing=True, pattern=r"love(?: |$)(,*)"))
async def _(event):
    await event.edit("**sayang**")
    sleep(2)
    await event.edit("**kamu udah makan belum**")
    slepp(3)
    await event.edit("** kalau belum sini aku suapin jiakhhh)
    
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
        \n\n  •  **Syntax :** `{cmd}love`\
        \n  •  **Function : **kemu udah makan belum\
        \n\n  •  **Syntax :** `{cmd}k`\
        \n  •  **Function : **nanyain kabar\
        \n\n  •  **Syntax :** `{cmd}j`\
        \n  •  **Function : **untuk gombalan\
    "
    }
)
