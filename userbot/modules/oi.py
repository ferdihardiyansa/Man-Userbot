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
    await event.edit("**jangan lupa berdoa**")
    sleep(2)
    await event.edit("**tidur nyenyak yah**")
    sleep(2)
    await event.edit("**mimpi indah yah**")
    sleep(3)
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


@bot.on(man_cmd(outgoing=True, pattern=r"gmbln(?: |$)(.*)"))
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
    await event.edit("**kamu mau tau cara putihin rambut secara permanen?**")
    sleep(4)
    await event.edit("**menualah bersamaku JIAKHHHH**")
    sleep(4)
    await event.edit("**JIAKHHHHHHHHHH**")


@bot.on(man_cmd(outgoing=True, pattern=r"sore(?: |$)(.*)"))
async def _(event):
    await event.edit("**selamat sore**")
    sleep(2)
    await event.edit("**Lewati sore harimu dengan duduk santai sambil memikirkan sesuatu yang indah**")
    sleep(4)
    await event.edit("**Terlalu fokus dalam pekerjaan apapun yang kalian lakukan hanya akan membuatmu melewati waktu berharga ini**")


@bot.on(man_cmd(outgoing=True, pattern=r"jangan(?: |$)(.*)"))
async def _(event):
    await event.edit("**LAIN KALI JANGAN BEGITU YAH EPERYBADY**")
    sleep(2)
    await event.edit("**WATEPAK MEN**")


@bot.on(man_cmd(outgoing=True, pattern=r"cuka(?: |$)(.*)"))
async def _(event):
    await event.edit("**cape cape nyari cuka di dapur**")
    sleep(2)
    await event.edit("**eh taunya cuka sama kamu**")


@bot.on(man_cmd(outgoing=True, pattern=r"telalu(?: |$)(.*)"))
async def _(event):
    await event.edit("**KAMU TERLALU CANTIK**")
    sleep(2)
    await event.edit("**WAH INI TIDAK ADIL**")
    sleep(3)
    await event.edit("**MANA MUNGKIN AKU TIDAK TERTARIK**")


@bot.on(man_cmd(outgoing=True, pattern=r"tahu(?: |$)(.*)"))
async def _(event):
    await event.edit("**tukang tahu makan ikahn hiu**")
    sleep(2)
    await event.edit("**GAK TAU POKOKNYA MAH I LOPE YOU**")
    sleep(2)
    await event.edit("**YOU LOVE ME TO GA?**")

@bot.on(man_cmd(outgoing=True, pattern=r"samyang(?: |$)(.*)"))
async def _(event):
    await event.edit("**tadikan aku beli samyang di indomaret**")
    sleep(2)
    await event.edit("**pas di cari gak ada**")
    sleep(2)
    await event.edit("**eh ternyata samyang sama kamu JIAKHHH**")


@bot.on(man_cmd(outgoing=True, pattern=r"gcs(?: |$)(.*)"))
async def _(event):
    if event.chat_id in BLACKLIST_CHAT:
        return await event.edit("**Perintah ini Dilarang digunakan di Group ini**")
    await event.client.send_message(
        event.chat_id, "**GC SAMPAH KAYA GINI, BUBARIN AJA GOBLOK!!**"
    )
    await event.delete()


@bot.on(man_cmd(outgoing=True, pattern=r"sdby(?: |$)(.*)"))
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
        \n\n  •  **Syntax :** `{cmd}gmbln`\
        \n  •  **Function : **kata kata menggombal\
        \n\n  •  **Syntax :** `{cmd}sdby`\
        \n  •  **Function : **gombalan versi 2\
        \n\n  •  **Syntax :** `{cmd}jauh`\
        \n  •  **Function : **sad\
        \n\n  •  **Syntax :** `{cmd}menua`\
        \n  •  **Function : **gmbln versi 3\
        \n\n  •  **Syntax :** `{cmd}sore`\
        \n  •  **Function : **selamat sore\
        \n\n  •  **Syntax :** `{cmd}jangan`\
        \n  •  **Function : **perkataan katak bizer\
        \n\n  •  **Syntax :** `{cmd}sokab`\
        \n  •  **Function : **Ngeledek orang so kenal so dekat padahal kga kenal goblok\
        \n\n  •  **Syntax :** `{cmd}terlalu`\
        \n  •  **Function : **ngegomabl cewe\
        \n\n  •  **Syntax :** `{cmd}tahu`\
        \n  •  **Function : **ngegombal juga\
        \n\n  •  **Syntax :** `{cmd}samyang`\
        \n  •  **Function : **ngegombal tentang samyang\
        \n\n  •  **Syntax :** `{cmd}gcs`\
        \n  •  **Function : **gc\
        \n\n  •  **Syntax :** `{cmd}virtual`\
        \n  •  **Function : **Ngeledek orang pacaran virtual\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
