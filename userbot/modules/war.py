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
    
    
@bot.on(man_cmd(outgoing=True, pattern=r"bocah(?: |$)(.*)"))
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**BOCAH LAKNAT DUNIA AKHIRAT ORANG TOLOL GAK PUNYA BAKAY DATENG KESINI SALAH ALAMAT MUKANYA KAYAK LINTAH DARAT SUKANYA JILAT JILAT PANTAT ORANG DASAR ORANG CACAT GIGI KUNING BERKARAT HIDUP MASIH MELARAT MEMANG DASAR SILUMAN BABI PERILAKU MISKIN MENJADI JADIORANG TUA LU MATI MALAH MENARI GOYANG DUA JARI**",
    )
    await event.delete()
    
    CMD_HELP.update(
    {
        "war": f"**Plugin : **`war`\
        \n\n  •  **Syntax :** `{cmd}buah`\
        \n  •  **Function : **kosa kata 1\
        \n\n  •  **Syntax :** `{cmd}bocah`\
        \n  •  **Function : **kosa kata 2\
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

    
