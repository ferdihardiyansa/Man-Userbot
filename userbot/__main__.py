# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Copyright (C) 2021 TeamUltroid for autobot
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
#
""" Userbot start point """

import glob
import sys
from importlib import import_module
from pathlib import Path

from pytgcalls import idle
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from telethon.tl.functions.channels import JoinChannelRequest

from userbot import ALIVE_NAME, BOT_VER, BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import LOGS, UPSTREAM_REPO_BRANCH, bot, call_py
from userbot.modules import ALL_MODULES
from userbot.utils import autobot, start_assistant

assistant = os.environ.get("BOTMODE", None)

INVALID_PH = (
    "\nERROR: Nomor Telepon yang kamu masukkan SALAH."
    "\nTips: Gunakan Kode Negara beserta nomornya atau periksa nomor telepon Anda dan coba lagi."
)

try:
    bot.start()
    call_py.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info(
    f"Jika {ALIVE_NAME} Membutuhkan Bantuan, Silahkan Gabung ke Grup https://t.me/SharingUserbot"
)

LOGS.info(f"Man-Userbot ⚙️ V{BOT_VER} [🔥 BERHASIL DIAKTIFKAN! 🔥]")


async def assistants():
    if assistant == "ON":
        path = "userbot/modules/assistant/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                try:
                    start_assistant(shortname.replace(".py", ""))
                except Exception as e:
                    print(e)
    else:
        LOGS.info("Assistant Not Loaded ")


bot.loop.run_until_complete(assistants())


async def man_userbot_on():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_message(
                BOTLOG_CHATID,
                f"🔥 **Man-Userbot Berhasil Di Aktifkan**\n━━\n➠ **Userbot Version -** `{BOT_VER}@{UPSTREAM_REPO_BRANCH}`\n➠ **Ketik** `{cmd}alive` **untuk Mengecheck Bot**\n━━",
            )
    except Exception as e:
        LOGS.info(str(e))
    # KALO LU NGEFORK LINK CH & GRUP PUNYA GUA NYA JANGAN DI HAPUS YA GOBLOK 😡
    try:
        await bot(JoinChannelRequest("@Lunatic0de"))
        await bot(JoinChannelRequest("@SharingUserbot"))
    except BaseException:
        pass


# JANGAN DI HAPUS GOBLOK 😡 LU COPY/EDIT AJA TINGGAL TAMBAHIN PUNYA LU
# DI HAPUS GUA GBAN YA 🥴 GUA TANDAIN LU AKUN TELENYA 😡
bot.loop.create_task(man_userbot_on())
bot.loop.create_task(autobot())
idle()
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
