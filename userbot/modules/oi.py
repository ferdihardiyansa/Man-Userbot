from time import sleep

from userbot import BLACKLIST_CHAT
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, bot
from userbot.events import man_cmd


@bot.on(man_cmd(outgoing=True, pattern=r"sayang(?: |$)(.*)"))
async def _(event):
    await event.edit("**Cuma Mau Bilang**")
    sleep(3)
    await event.edit("**Aku Sayang Kamu**")
    sleep(1)
    await event.edit("**I LOVE YOU 💞**")


# Create by myself @localheart


@bot.on(man_cmd(outgoing=True, pattern=r"semangat(?: |$)(.*)"))
async def _(event):
    await event.edit("**Apapun Yang Terjadi**")
    sleep(3)
    await event.edit("**Tetaplah Bernapas**")
    sleep(1)
    await event.edit("**Dan Selalu Bersyukur**")


# Create by myself @localheart


@bot.on(man_cmd(outgoing=True, pattern=r"ywc(?: |$)(.*)"))
async def _(event):
    await event.client.send_message(event.chat_id, "**Ok Sama Sama**")
    await event.delete()


@bot.on(man_cmd(outgoing=True, pattern=r"pagi(?: |$)(.*)"))
async def _(event):
    await event.edit("**selamat pagi**")
    sleep(2)
    await event.edit("**jangan lupa sarapan**")
    sleep(2)
    await event.edit("**aku disini ada untukmu kok😃**")


@bot.on(man_cmd(outgoing=True, pattern=r"siang(?: |$)(.*)"))
async def _(event):
    await event.edit("**selamat siang**")
    sleep(2)
    await event.edit("**Aku berdoa agar siang harimu dipenuhi dengan berkah dan cinta**")
    sleep(2)
    await event.edit("**tetap semangat😊**")


@bot.on(man_cmd(outgoing=True, pattern=r"malam(?: |$)(.*)"))
async def _(event):
    await event.edit("**selamat malam**")
    sleep(2)
    await event.edit("**jangan lupa bedoa**")
    sleep(2)
    await event.edit("**tidur nyenyak yah**")
    sleep(2)
    await event.edit("**GOOD NIGHT**")
    

@bot.on(man_cmd(outgoing=True, pattern=r"aku(?: |$)(.*)"))
async def _(event):
    await event.edit("**aku bukanlah untukmu**")
    sleep(2)
    await event.edit("**tapi aku hanya ada untuk menghiburmu🤡**")


@bot.on(man_cmd(outgoing=True, pattern=r"ayam(?: |$)(.*)"))
async def _(event):
    await event.edit("**AYAM BERKOKOK NAIK DI GENTENG**")
    sleep(2)
    await event.edit("**TAK MEROKOK TAK GANTENG**")


@bot.on(man_cmd(outgoing=True, pattern=r"muter(?: |$)(.*)"))
async def _(event):
    await event.edit("**muter muter nyari matcha latte**")
    sleep(2)
    await event.edit("**eh nemunya matcha depan jiakhhhh**")
    

@bot.on(man_cmd(outgoing=True, pattern=r"jauh(?: |$)(.*)"))
async def _(event):
    await event.edit("**aku menjauh dulu yah**")
    sleep(2)
    await event.edit("**pengen perbaikin diri biar pantes sama kamu**")
    sleep(3)
    await event.edit("**tapi kalau kamu udah dapetin yg terbaik menurut kamu gpp aku ikut seneng kok😊**")


@bot.on(man_cmd(outgoing=True, pattern=r"menua(?: |$)(.*)"))
async def _(event):
    await event.edit("**kamu mau tau cara putihin rambut secaran permanen?**")
    sleep(3)
    await event.edit("**menualah bersamaku JIAKHHHH**")


@bot.on(man_cmd(outgoing=True, pattern=r"sore(?: |$)(.*)"))
async def _(event):
    await event.edit("**selamat sore**")
    sleep(2)
    await event.edit("**Lewati sore hari dengan duduk santai sambil memikirkan sesuatu yang indah**")
    sleep(3)
    await event.edit("**Terlalu fokus dalam pekerjaan apapun yang kalian lakukan hanya akan membuatmu melewati waktu berharga ini**")


@bot.on(man_cmd(outgoing=True, pattern=r"ded(?: |$)(.*)"))
async def _(event):
    await event.client.send_message(
        event.chat_id, "**MATI AJA LU GOBLOK, GAGUNA LU HIDUP DI BUMI**"
    )
    await event.delete()


@bot.on(man_cmd(outgoing=True, pattern=r"sokab(?: |$)(.*)"))
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**SOKAB BET LU GOBLOK, KAGA ADA ISTILAH NYA BAWAHAN TEMENAN AMA BOS!!**",
    )
    await event.delete()


@bot.on(man_cmd(outgoing=True, pattern=r"gembel(?: |$)(.*)"))
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**MUKA BAPAK LU KEK KELAPA SAWIT ANJING, GA USAH NGATAIN ORANG, MUKA LU AJA KEK GEMBEL TEXAS GOBLOK!!**",
    )
    await event.delete()


@bot.on(man_cmd(outgoing=True, pattern=r"cuih(?: |$)(.*)"))
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**GAK KEREN LO KEK BEGITU GOBLOK, KELUARGA LU BAWA SINI GUA LUDAHIN SATU-SATU. CUIHH!!!**",
    )
    await event.delete()


@bot.on(man_cmd(outgoing=True, pattern=r"dih(?: |$)(.*)"))
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**DIHHH NAJISS ANAK HARAM LO GOBLOK, JANGAN BELAGU DIMARI KAGA KEREN LU KEK BGITU TOLOL!**",
    )
    await event.delete()


@bot.on(man_cmd(outgoing=True, pattern=r"gcs(?: |$)(.*)"))
async def _(event):
    if event.chat_id in BLACKLIST_CHAT:
        return await event.edit("**Perintah ini Dilarang digunakan di Group ini**")
    await event.client.send_message(
        event.chat_id, "**GC SAMPAH KAYA GINI, BUBARIN AJA GOBLOK!!**"
    )
    await event.delete()


@bot.on(man_cmd(outgoing=True, pattern=r"gmbl(?: |$)(.*)"))
async def _(event):
    await event.edit("**aku tidak pernah bisa mengatakan betapa aku menyukaimu dan betapa istimewanya kamu untukku**")
    sleep(3)
    await event.edit("**tapi aku bisa mengatakan bahwa duniaku tersenyum setiap bersamamu**")


@bot.on(man_cmd(outgoing=True, pattern=r"virtual(?: |$)(.*)"))
async def _(event):
    await event.edit("**OOOO**")
    sleep(1.5)
    await event.edit("**INI YANG VIRTUAL**")
    sleep(1.5)
    await event.edit("**YANG KATANYA SAYANG BANGET**")
    sleep(1.5)
    await event.edit("**TAPI TETEP AJA DI TINGGAL**")
    sleep(1.5)
    await event.edit("**NI INGET**")
    sleep(1.5)
    await event.edit("**TANGANNYA AJA GA BISA DI PEGANG**")
    sleep(1.5)
    await event.edit("**APALAGI OMONGANNYA**")
    sleep(1.5)
    await event.edit("**BHAHAHAHA**")
    sleep(1.5)
    await event.edit("**KASIAN MANA MASIH MUDA**")


CMD_HELP.update(
    {
        "kabar": f"**Plugin : **`kabar`\
        \n\n  •  **Syntax :** `{cmd}pagi`\
        \n  •  **Function : **selamat pagi\
        \n\n  •  **Syntax :** `{cmd}siang`\
        \n  •  **Function : **selamat siang\
        \n\n  •  **Syntax :** `{cmd}malam`\
        \n  •  **Function : **selamat malam\
        \n\n  •  **Syntax :** `{cmd}aku`\
        \n  •  **Function : **kata kata badut\
        \n\n  •  **Syntax :** `{cmd}ayam`\
        \n  •  **Function : **pantun\
        \n\n  •  **Syntax :** `{cmd}muter`\
        \n  •  **Function : **kata kata menggombal\
        \n\n  •  **Syntax :** `{cmd}gmbl`\
        \n  •  **Function : **gombalan versi 2\
        \n\n  •  **Syntax :** `{cmd}jauh`\
        \n  •  **Function : **sad\
        \n\n  •  **Syntax :** `{cmd}menua`\
        \n  •  **Function : **gmbln versi 3\
        \n\n  •  **Syntax :** `{cmd}sore`\
        \n  •  **Function : **selamat sore\
        \n\n  •  **Syntax :** `{cmd}ded`\
        \n  •  **Function : **Nyuruh orang mati aja goblok wkwk\
        \n\n  •  **Syntax :** `{cmd}sokab`\
        \n  •  **Function : **Ngeledek orang so kenal so dekat padahal kga kenal goblok\
        \n\n  •  **Syntax :** `{cmd}gembel`\
        \n  •  **Function : **Ngeledek bapaknya si jamet\
        \n\n  •  **Syntax :** `{cmd}cuih`\
        \n  •  **Function : **Ngeludahin keluarganya satu satu wkwk\
        \n\n  •  **Syntax :** `{cmd}dih`\
        \n  •  **Function : **Ngeledek anak haram\
        \n\n  •  **Syntax :** `{cmd}gcs`\
        \n  •  **Function : **Ngeledek gc sampah\
        \n\n  •  **Syntax :** `{cmd}virtual`\
        \n  •  **Function : **Ngeledek orang pacaran virtual\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
