from time import sleep

from userbot import ALIVE_NAME
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, bot
from userbot.events import man_cmd


@bot.on(man_cmd(outgoing=True, pattern="p(?: |$)(.*)"))
async def _(event):
    await event.edit("**PUNTEN SLURRRR**")
    sleep(2)
    await event.edit("**ASSALAMUALAIKUM UKHTI**")


@bot.on(man_cmd(outgoing=True, pattern="makan(?: |$)(.*)"))
async def _(event):
    await event.edit("**KAMU UDAH MAKAN BELUM**")
    sleep(2)
    await event.edit("**KALAU BELUM MATI AJA SEKALIAN**")
    sleep(3)
    await  event.edit("**BECANDA**")
   

@bot.on(man_cmd(outgoing=True, pattern=r"pe(?: |$)(.*)"))
async def _(event):
    await event.edit("**PUNTEN MAMANG**")
    sleep(2)
    await event.edit("**ASSALAMUALAIKUM**")


@bot.on(man_cmd(outgoing=True, pattern="jawab(?: |$)(.*)"))
async def _(event):
    await event.edit(f"**Haii Salken Saya {ALIVE_NAME}**")
    sleep(2)
    await event.edit("**wa'laikumsalam**")


@bot.on(man_cmd(outgoing=True, pattern=r"sama(?: |$)(.*)"))
async def _(event):
    await event.edit("**SAMA SAMA SAYANG**")


@bot.on(man_cmd(outgoing=True, pattern=r"gombalan(?: |$)(.*)"))
async def _(event):
    await event.edit("**IKAN HIU MELAYANG LAYANG**")
    sleep(2)
    await event.edit("**I LOVE YOU SAYANG JIAKHHH**")


@bot.on(man_cmd(outgoing=True, pattern=r"kabar(?: |$)(.*)"))
async def _(event):
    await event.edit(f"** HALLO **")
    sleep(2)
    await event.edit("**GIMANA KABARNYA?**")


@bot.on(man_cmd(outgoing=True, pattern=r"wala(?: |$)(.*)"))
async def _(event):
    await event.edit("**w**")
    sleep(0.5)
    await event.edit("**wa**")
    sleep(0.5)
    await event.edit("**waa**")
    sleep(0.5)
    await event.edit("**waal**")
    sleep(0.5)
    await event.edit("**waala**")
    sleep(0.5)
    await event.edit("**waalai**")
    sleep(0.5)
    await event.edit("**waalaik**")
    sleep(0.5)
    await event.edit("**waalaiku**")
    sleep(0.5)
    await event.edit("**waalaikum**")
    sleep(0.5)
    await event.edit("**waalaikums**")
    sleep(0.5)
    await event.edit("**waalaikumsa**")
    sleep(0.5)
    await event.edit("**waalaikumsal**")
    sleep(0.5)
    await event.edit("**waalaikumsala**")
    sleep(0.5)
    await event.edit("**waalaikumsalam**")
    
    

@bot.on(man_cmd(outgoing=True, pattern=r"cukup(?: |$)(.*)"))
async def _(event):
    await event.edit("**my happiness?**")
    sleep(3)
    await event.edit("**cukup**")
    sleep(1)
    await event.edit("**CUKUP KAU DI SAMPING KU**")
    sleep(4)
    await event.edit("**SEMPURNAHKAN LANGKAH KU TUK MENYUSURI WAKTU**")
    sleep(3)
    await event.edit("**CUKUP KAU DI SAMPING KU**")
    sleep(3)
    await event.edit("**BERJALAN BERSAMA KU PASTIKAN KAU BAHAGIA**")
    
    
CMD_HELP.update(
    {
        "salam": f"**Plugin : **`salam`\
        \n\n  •  **Syntax :** `{cmd}p`\
        \n  •  **Function : **Assalamualaikum Dulu Biar Sopan..\
        \n\n  •  **Syntax :** `{cmd}pe`\
        \n  •  **Function : **salam Kenal dan salam\
        \n\n  •  **Syntax :** `{cmd}sama`\
        \n  •  **Function : **nMenampilkan sama sama syang\
        \n\n  •  **Syntax :** `{cmd}makan`\
        \n  •  **Function : ** `nanyain kabar makan`\
        \n\n  •  **Syntax :** `{cmd}kabar`\
        \n  •  **Function : **nanyain kabar\
        \n\n  •  **Syntax :** `{cmd}gombalan`\
        \n  •  **Function : **untuk gombalan\
        \n\n  •  **Syntax :** `{cmd}cukup`\
        \n  •  **Function : **nyanyi lagunya rizky febian\
     "
    }
)
