from time import sleep

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, owner
from userbot.utils import edit_or_reply, man_cmd


@man_cmd(pattern="p(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**PUNTEN SLURRRR**")
    sleep(2)
    await edit_or_reply(event, "**ASSALAMUALAIKUM UKHTI**")


@man_cmd(pattern="makan(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**KAMU UDAH MAKAN BELUM**")
    sleep(2)
    await edit_or_reply(event, "**KALAU BELUM MATI AJA SEKALIAN**")
    sleep(3)
    await edit_or_reply(event, "**BECANDA**")
   

@man_cmd(pattern="pe(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**PUNTEN MAMANG**")
    sleep(2)
    await edit_or_reply(event, "**ASSALAMUALAIKUM**")


@man_cmd(pattern="jawab(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**Haii Salken Saya {owner}**")
    sleep(2)
    await xx.edit("**Assalamualaikum...**")


@man_cmd(pattern="sama(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**SAMA SAMA SAYANG**")


@man_cmd(pattern="gabut(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**IKAN HIU MELAYANG LAYANG**")
    sleep(2)
    await edit_or_reply(event, "**I LOVE YOU SAYANG JIAKHHH**")


@man_cmd(pattern="kabar(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**HALLO**")
    sleep(2)
    await edit_or_reply(event, "**GIMANA KABARNYA?**")


@man_cmd(pattern="wala(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**w**")
    sleep(0.5)
    await edit_or_reply(event, "**wa**")
    sleep(0.5)
    await edit_or_reply(event, "**waa**")
    sleep(0.5)
    await edit_or_reply(event, "**waal**")
    sleep(0.5)
    await edit_or_reply(event, "**waala**")
    sleep(0.5)
    await edit_or_reply(event, "**waalai**")
    sleep(0.5)
    await edit_or_reply(event, "**waalaik**")
    sleep(0.5)
    await edit_or_reply(event, "**waalaiku**")
    sleep(0.5)
    await edit_or_reply(event, "**waalaikum**")
    sleep(0.5)
    await edit_or_reply(event, "**waalaikums**")
    sleep(0.5)
    await edit_or_reply(event, "**waalaikumsa**")
    sleep(0.5)
    await edit_or_reply(event, "**waalaikumsal**")
    sleep(0.5)
    await edit_or_reply(event, "**waalaikumsala**")
    sleep(0.5)
    await edit_or_reply(event, "**waalaikumsalam**")
    
    

@man_cmd(pattern="cukup(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**my happiness?**")
    sleep(3)
    await edit_or_reply(event, "**cukup**")
    sleep(1)
    await edit_or_reply(event, "**CUKUP KAU DI SAMPING KU**")
    sleep(4)
    await edit_or_reply(event, "**SEMPURNAHKAN LANGKAH KU TUK MENYUSURI WAKTU**")
    sleep(3)
    await edit_or_reply(event, "**CUKUP KAU DI SAMPING KU**")
    sleep(3)
    await edit_or_reply(event, "**BERJALAN BERSAMA KU PASTIKAN KAU BAHAGIA**")
    
    
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
        \n\n  •  **Syntax :** `{cmd}gabut`\
        \n  •  **Function : **coba aja\
        \n\n  •  **Syntax :** `{cmd}wala`\
        \n  •  **Function : **waalaikumsalam\
        \n\n  •  **Syntax :** `{cmd}cukup`\
        \n  •  **Function : **nyanyi lagunya rizky febian\
     "
    }
)
