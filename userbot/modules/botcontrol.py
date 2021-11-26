# Copyright (C) 2021 Catuserbot <https://github.com/sandy1709/catuserbot>
# Ported by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import io
import re
from datetime import datetime

from telethon import Button, custom
from telethon.utils import get_display_name

from userbot import BOT_USERNAME, BOTLOG, BOTLOG_CHATID, CHANNEL, GROUP, tgbot, user
from userbot.modules.sql_helper.bot_blacklists import check_is_black_list
from userbot.modules.sql_helper.bot_starters import (
    add_starter_to_db,
    get_all_starters,
    get_starter_details,
)
from userbot.modules.sql_helper.globals import gvarstatus
from userbot.utils import _format, asst_cmd, callback, reply_id

botusername = BOT_USERNAME
OWNER = user.first_name
OWNER_ID = user.id


async def check_bot_started_users(user, event):
    if user.id == OWNER_ID:
        return
    check = get_starter_details(user.id)
    if check is None:
        start_date = str(datetime.now().strftime("%B %d, %Y"))
        notification = f"🔮 **#BOT_START**\n**First Name:** {_format.mentionuser(user.first_name , user.id)} \
                \n**User ID: **`{user.id}`\
                \n**Action: **Telah Memulai saya."
    else:
        start_date = check.date
        notification = f"🔮 **#BOT_RESTART**\n**First Name:** {_format.mentionuser(user.first_name , user.id)}\
                \n**ID: **`{user.id}`\
                \n**Action: **Telah Me-Restart saya"
    try:
        add_starter_to_db(user.id, get_display_name(user), start_date, user.username)
    except Exception as e:
        LOGS.error(str(e))
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, notification)


@callback(data=re.compile(b"pmclose"))
async def users(event):
    if event.query.user_id == OWNER_ID:
        await event.delete()


@callback(data=re.compile(b"pmbot"))
async def help(event):
    await event.delete()
    if event.query.user_id == OWNER_ID:
        await tgbot.send_message(
            event.chat_id,
            message=f"""**Perintah di Bot ini adalah:**\n
**NOTE: Perintah ini hanya berfungsi di {botusername}**\n
 • **Command : **/uinfo <reply ke pesan>
 • **Function : **Untuk Mencari Info Pengirim Pesan.\n
 • **Command : **/ban <alasan> atau /ban <username/userid> <alasan>
 • **Function : **Untuk Membanned Pengguna dari BOT.(Gunakan alasan saat ban)\n
 • **Command : **/unban <alasan> atau /unban <username/userid>
 • **Function : **Membuka Banned pengguna dari bot, agar bisa mengirim pesan lagi dibot.
 • **NOTE : **Untuk memeriksa daftar pengguna yang dibanned Ketik `.bblist`\n
 • **Command : **/broadcast
 • **Function : **Balas ke pesan untuk diBroadcast ke setiap pengguna yang memulai bot Anda. Untuk mendapatkan daftar pengguna Ketik `.botuser`\n
 • **NOTE : ** Jika pengguna menghentikan/memblokir bot maka dia akan dihapus dari database Anda yaitu dia akan dihapus dari daftar bot_starters
""",
            buttons=[
                [
                    custom.Button.inline(
                        "ᴄʟᴏsᴇ",
                        data="pmclose",
                    )
                ],
            ],
        )


@callback(data=re.compile(b"users"))
async def users(event):
    if event.query.user_id == OWNER_ID:
        await event.delete()
        total_users = get_all_starters()
        msg = "**Daftar Pengguna Di Bot** \n\n"
        for user in total_users:
            msg += f"• **First Name:** {_format.mentionuser(user.first_name , user.user_id)}\n**User ID:** `{user.user_id}`\n**Tanggal: **{user.date}\n\n"
        with io.BytesIO(str.encode(msg)) as fileuser:
            fileuser.name = "userlist.txt"
            await tgbot.send_file(
                event.chat_id,
                fileuser,
                force_document=True,
                caption="**Total Pengguna Di Bot anda.**",
                allow_cache=False,
            )
    else:
        pass


@asst_cmd(pattern=f"^/start({botusername})?([\\s]+)?$", func=lambda e: e.is_private)
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
                    f"https://t.me/{CHANNEL}"
                ),
            )
        ]
    else:
        start_msg = f"**Halo [{OWNER}](tg://user?id={OWNER_ID})**\
            \n**Apa ada yang bisa saya Bantu?**"
        buttons = [
            (
                Button.inline("ᴘᴍʙᴏᴛ", data="pmbot"),
                Button.inline("ᴜsᴇʀs", data="users"),
            ),
            (Button.inline("ᴄʟᴏsᴇ", data="pmclose"),),
        ]
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
