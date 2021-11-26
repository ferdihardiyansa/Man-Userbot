import asyncio
import os
import random
import re
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError

from userbot.utils import ass_cmd
from userbot import tgbot

spam_chats = []


@ass_cmd(pattern="^/tagall|/call|/tall|/all|/mentionall|#all|@all ?(.*)")
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.reply(
            "**Perintah ini hanya dapat digunakan dalam grup dan channel!**"
        )

    is_admin = False
    try:
        partici_ = await tgbot(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.reply("**Hanya admin yang bisa mention semua Member!**")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.reply("**Beri saya satu Tambahan Text!**")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg is None:
            return await event.reply(
                "**Saya tidak bisa menyebut anggota untuk pesan lama! (pesan yang dikirim sebelum saya ditambahkan ke grup)**"
            )
    else:
        return await event.reply(
            "**Balas pesan atau Beri saya beberapa teks untuk mention orang lain!**"
        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in tgbot.iter_participants(chat_id):
        if chat_id not in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}), "
        if usrnum == 5:
            if mode == "text_on_cmd":
                txt = f"{msg}\n{usrtxt}"
                await tgbot.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except BaseException:
        pass


@ass_cmd(pattern="^/cancel$")
async def cancel_spam(event):
    if event.chat_id not in spam_chats:
        return await event.reply("**Tidak ada proses Mention yang Sedang berjalan...**")
    else:
        try:
            spam_chats.remove(event.chat_id)
        except BaseException:
            pass
        return await event.reply("**MemBerhentikan Mention all**")
