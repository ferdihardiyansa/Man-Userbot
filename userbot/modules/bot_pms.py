# Copyright (C) 2021 Catuserbot <https://github.com/sandy1709/catuserbot>
# Ported by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

from datetime import datetime

from telethon import Button, events
from telethon.errors import UserIsBlockedError
from telethon.utils import get_display_name

from userbot import BOT_USERNAME, BOTLOG, BOTLOG_CHATID, CHANNEL, GROUP, tgbot, user
from userbot.modules.sql_helper.bot_blacklists import check_is_black_list
from userbot.modules.sql_helper.bot_pms_sql import add_user_to_db, get_user_id
from userbot.modules.sql_helper.bot_starters import (
    add_starter_to_db,
    get_starter_details,
)
from userbot.modules.sql_helper.globals import gvarstatus
from userbot.utils import _format, reply_id
from userbot.utils.logger import logging

LOGS = logging.getLogger(__name__)

botusername = BOT_USERNAME
OWNER_ID = user.id
OWNER = user.first_name


async def check_bot_started_users(user, event):
    if user.id == OWNER_ID:
        return
    check = get_starter_details(user.id)
    if check is None:
        start_date = str(datetime.now().strftime("%B %d, %Y"))
        notification = f"**First Name:** {_format.mentionuser(user.first_name , user.id)} \
                \n**User ID: **`{user.id}`\
                \n**Action: **Telah Memulai saya."
    else:
        start_date = check.date
        notification = f"**First Name:** {_format.mentionuser(user.first_name , user.id)}\
                \n**ID: **`{user.id}`\
                \n**Action: **Telah Me-Restart saya"
    try:
        add_starter_to_db(user.id, get_display_name(user), start_date, user.username)
    except Exception as e:
        LOGS.error(str(e))
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, notification)


@tgbot.on(
    events.NewMessage(
        pattern=f"^/start({botusername})?([\\s]+)?$", func=lambda e: e.is_private
    )
)
async def bot_start(event):
    chat = await event.get_chat()
    user = await event.client.get_me()
    if check_is_black_list(chat.id):
        return
    reply_to = await reply_id(event)
    mention = f"[{chat.first_name}](tg://user?id={chat.id})"
    my_mention = f"[{user.first_name}](tg://user?id={user.id})"
    first = chat.first_name
    last = chat.last_name
    fullname = f"{first} {last}" if last else first
    username = f"@{chat.username}" if chat.username else mention
    userid = chat.id
    my_first = user.first_name
    my_last = user.last_name
    my_fullname = f"{my_first} {my_last}" if my_last else my_first
    my_username = f"@{user.username}" if user.username else my_mention
    if chat.id != OWNER_ID:
        customstrmsg = gvarstatus("START_TEXT") or None
        if customstrmsg is not None:
            start_msg = customstrmsg.format(
                mention=mention,
                first=first,
                last=last,
                fullname=fullname,
                username=username,
                userid=userid,
                my_first=my_first,
                my_last=my_last,
                my_fullname=my_fullname,
                my_username=my_username,
                my_mention=my_mention,
            )
        else:
            start_msg = f"**👋 Hai** {mention}**!**\
                        \n\n**Saya adalah {my_first}** \
                        \n**Anda dapat Menghubungi [{OWNER}](tg://user?id={OWNER_ID}) dari sini.**\
                        \n**Jangan Melakukan Spam Atau anda akan diBanned**\
                        \n\n**Powered by** [UserBot](https://github.com/mrismanaziz/Man-Userbot)"
        buttons = [
            (
                Button.url("ɢʀᴏᴜᴘ", f"https://t.me/{GROUP}"),
                Button.url(
                    "ᴄʜᴀɴɴᴇʟ",
                    f"https://t.me/{CHANNEL}",
                ),
            )
        ]
    else:
        start_msg = "**Halo Master!\
            \nApa ada yang bisa saya Bantu?\
            \nSilahkan Ketik /help Bila butuh Bantuan**"
        buttons = None
    try:
        await event.client.send_message(
            chat.id,
            start_msg,
            link_preview=False,
            buttons=buttons,
            reply_to=reply_to,
        )
    except Exception as e:
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**ERROR:** Saat Pengguna memulai Bot anda.\\\x1f                \n`{e}`",
            )

    else:
        await check_bot_started_users(chat, event)


@tgbot.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def bot_pms(event):
    chat = await event.get_chat()
    if check_is_black_list(chat.id):
        return
    if chat.id != OWNER_ID:
        msg = await event.forward_to(OWNER_ID)
        try:
            add_user_to_db(msg.id, get_display_name(chat), chat.id, event.id, 0, 0)
        except Exception as e:
            LOGS.error(str(e))
            if BOTLOG:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    f"**ERROR:** Saat menyimpan detail pesan di database\n`{str(e)}`",
                )
    else:
        if event.text.startswith("/"):
            return
        reply_to = await reply_id(event)
        if reply_to is None:
            return
        users = get_user_id(reply_to)
        if users is None:
            return
        for usr in users:
            user_id = int(usr.chat_id)
            reply_msg = usr.reply_id
            user_name = usr.first_name
            break
        if user_id is not None:
            try:
                if event.media:
                    msg = await event.client.send_file(
                        user_id, event.media, caption=event.text, reply_to=reply_msg
                    )
                else:
                    msg = await event.client.send_message(
                        user_id, event.text, reply_to=reply_msg, link_preview=False
                    )
            except UserIsBlockedError:
                return await event.reply("❌ 𝗧𝗵𝗶𝘀 𝗯𝗼𝘁 𝘄𝗮𝘀 𝗯𝗹𝗼𝗰𝗸𝗲𝗱 𝗯𝘆 𝘁𝗵𝗲 𝘂𝘀𝗲𝗿.")
            except Exception as e:
                return await event.reply(f"**ERROR:** `{e}`")
            try:
                add_user_to_db(
                    reply_to, user_name, user_id, reply_msg, event.id, msg.id
                )
            except Exception as e:
                LOGS.error(str(e))
                if BOTLOG:
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        f"**ERROR:** Saat menyimpan detail pesan di database\n`{e}`",
                    )


@tgbot.on(events.NewMessage(pattern="^/uinfo$", from_users=OWNER_ID))
async def bot_start(event):
    reply_to = await reply_id(event)
    if not reply_to:
        return await event.reply(
            "**Silahkan Balas ke pesan untuk mendapatkan info pesan**"
        )
    info_msg = await event.client.send_message(
        event.chat_id,
        "`🔎 Sedang Mencari di Database...`",
        reply_to=reply_to,
    )
    users = get_user_id(reply_to)
    if users is None:
        return await info_msg.edit(
            "**ERROR: Maaf! Tidak Dapat Menemukan pengguna ini di database saya 🥺**"
        )
    for usr in users:
        user_id = int(usr.chat_id)
        user_name = usr.first_name
        break
    if user_id is None:
        return await info_msg.edit(
            "**ERROR: Maaf! Tidak Dapat Menemukan pengguna ini di database saya 🥺**"
        )
    uinfo = f"**Pesan ini dikirim oleh**\
            \n**First Name:** {_format.mentionuser(user_name , user_id)}\
            \n**User ID:** `{user_id}`"
    await info_msg.edit(uinfo)
