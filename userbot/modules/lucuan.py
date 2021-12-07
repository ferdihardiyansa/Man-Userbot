from time import sleep

from userbot import ALIVE_NAME
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, bot
from userbot.events import man_cmd


@bot.on(man_cmd(outgoing=True, pattern="anda(?: |$)(.*)"))
async def _(event):
    await event.edit("**anda sopan kami curiga**")
    sleep(2)
    await event.edit("**hmmm🤔**")


@bot.on(man_cmd(outgoing=True, pattern="motor(?: |$)(.*)"))
async def _(event):
    await event.edit("**Kalo naik motor sama kamu pasti ditilang polisi deh**")
    sleep(2)
    await event.edit("**Soalnya kita selalu bertiga**")
    sleep(2)
    await event.edit("**aku, kamu, dan cinta**")
   

@bot.on(man_cmd(outgoing=True, pattern=r"pcr(?: |$)(.*)"))
async def _(event):
    await event.edit("**Sebenarnya pacar orang itu juga pacar kita**")
    sleep(2)
    await event.edit("**karena kita kan juga orang**")
    sleep(2)
    await event.edit("**bener ga?**")


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
        "lucu": f"**Plugin : **`lucu`\
        \n\n  •  **Syntax :** `{cmd}anda`\
        \n  •  **Function : **mencurigakan\
        \n\n  •  **Syntax :** `{cmd}motor`\
        \n  •  **Function : **gombalan motor\
        \n\n  •  **Syntax :** `{cmd}pcr`\
        \n  •  **Function : **untuk lucuan pacar kita juga\
        \n\n  •  **Syntax :** `{cmd}ass`\
        \n  •  **Function : **Salam Bahas arab\
        \n\n  •  **Syntax :** `{cmd}`\
        \n  •  **Function : **nMenampilkan sama sama syang\
        \n\n  •  **Syntax :** `{cmd}makan`\
        \n  •  **Function : ** `nanyain kabar makan`\
        \n\n  •  **Syntax :** `{cmd}k`\
        \n  •  **Function : **nanyain kabar\
        \n\n  •  **Syntax :** `{cmd}gombalan`\
        \n  •  **Function : **untuk gombalan\
        \n\n  •  **Syntax :** `{cmd}cukup`\
        \n  •  **Function : **nyanyi lagunya rizky febian\
     "
    }
)
