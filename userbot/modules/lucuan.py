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
    sleep(3)
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


@bot.on(man_cmd(outgoing=True, pattern="setan(?: |$)(.*)"))
async def _(event):
    await event.edit(f"**Entah mengapa di saat aku menyebut setan, mereka mengatakan bahwa itu kasar**")
    sleep(3)
    await event.edit("**padahal setan kan makhluk halus.**")
    sleep(2.5)
    await event.edit("**benerkan?**")


@bot.on(man_cmd(outgoing=True, pattern=r"pinjem(?: |$)(.*)"))
async def _(event):
    await event.edit("**Eh pinjem flashdisk dong**")
    sleep(2)
    await event.edit("**aku pengen transfer data cintaku buat kamu**")


@bot.on(man_cmd(outgoing=True, pattern=r"ganteng(?: |$)(.*)"))
async def _(event):
    await event.edit("**kamu itu ganteng tapi sayang**")
    sleep(2)
    await event.edit("**bukan punyaku**")


@bot.on(man_cmd(outgoing=True, pattern=r"cantik(?: |$)(.*)"))
async def _(event):
    await event.edit("**kamu cantik tapi sayang**")
    sleep(2)
    await event.edit("**bukan punyaku**")


@bot.on(man_cmd(outgoing=True, pattern=r"pocong(?: |$)(.*)"))
async def _(event):
    await event.edit("**Kalo nanti malam ada pocong ngintip di jendela**")
    sleep(3)
    await event.edit("** jangan takut yah**")
    sleep(2)
    await event.edit("**dia memang sengaja aku suruh untuk jagain kamu bobo**")
    
    

@bot.on(man_cmd(outgoing=True, pattern=r"empat(?: |$)(.*)"))
async def _(event):
    await event.edit("**Empat dikali empat sama dengan enam belas**")
    sleep(3)
    await event.edit("**Cepat atau lambat, cintaku pasti kau balas**")
    
    
CMD_HELP.update(
    {
        "gombal": f"**Plugin : **`gombalan`\
        \n\n  •  **Syntax :** `{cmd}anda`\
        \n  •  **Function : **mencurigakan\
        \n\n  •  **Syntax :** `{cmd}motor`\
        \n  •  **Function : **gombalan motor\
        \n\n  •  **Syntax :** `{cmd}pcr`\
        \n  •  **Function : **untuk lucuan pacar kita juga\
        \n\n  •  **Syntax :** `{cmd}setan`\
        \n  •  **Function : **lawakan tentang setan\
        \n\n  •  **Syntax :** `{cmd}ganteng`\
        \n  •  **Function : **ganteng tapi sayg bukan punyaku\
        \n\n  •  **Syntax :** `{cmd}cantik`\
        \n  •  **Function : **cantik tapi sayang bukan punyaku\
        \n\n  •  **Syntax :** `{cmd}pinjem`\
        \n  •  **Function : **gombalan tentang flashdisk\
        \n\n  •  **Syntax :** `{cmd}pocong\
        \n  •  **Function : **gombalan tentang pocong\
        \n\n  •  **Syntax :** `{cmd}empat`\
        \n  •  **Function : **gombalan pantun\
     "
    }
)
