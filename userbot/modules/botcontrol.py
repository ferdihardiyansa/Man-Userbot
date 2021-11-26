# Copyright (C) 2021 Catuserbot <https://github.com/sandy1709/catuserbot>
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import io
import re
import time
from datetime import datetime

import heroku3
from telethon import Button, custom
from telethon.utils import get_display_name, pack_bot_file_id

from userbot import (
    ALIVE_NAME,
    BOT_USERNAME,
    BOTLOG,
    BOTLOG_CHATID,
    CHANNEL,
    GROUP,
    HEROKU_API_KEY,
    HEROKU_APP_NAME,
    StartTime,
    tgbot,
    user,
)
from userbot.modules.sql_helper.bot_blacklists import check_is_black_list
from userbot.modules.sql_helper.bot_starters import (
    add_starter_to_db,
    get_all_starters,
    get_starter_details,
)
from userbot.modules.sql_helper.globals import gvarstatus
from userbot.utils import _format, asst_cmd, callback, reply_id

from .ping import get_readable_time

botusername = BOT_USERNAME
OWNER = user.first_name
OWNER_ID = user.id


heroku_api = "https://api.heroku.com"
if HEROKU_APP_NAME is not None and HEROKU_API_KEY is not None:
    Heroku = heroku3.from_key(HEROKU_API_KEY)
    app = Heroku.app(HEROKU_APP_NAME)
    heroku_var = app.config()
else:
    app = None


async def setit(event, name, value):
    try:
        heroku_var[name] = value
    except BaseException:
        return await event.edit("**Maaf Gagal Menyimpan Karena ERROR**")


def get_back_button(name):
    button = [Button.inline("« ʙᴀᴄᴋ", data=f"{name}")]
    return button


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
async def pmclose(event):
    if event.query.user_id == OWNER_ID:
        await event.delete()


@callback(data=re.compile(b"pmbot"))
async def pmbot(event):
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
                        "ʙᴀᴄᴋ",
                        data="settings",
                    )
                ],
            ],
        )


@callback(data=re.compile(b"users"))
async def users(event):
    await event.delete()
    if event.query.user_id == OWNER_ID:
        total_users = get_all_starters()
        msg = "Daftar Pengguna Di Bot \n\n"
        for user in total_users:
            msg += f"• First Name: {user.first_name}\nUser ID: {user.user_id}\nTanggal: {user.date}\n\n"
        with io.BytesIO(str.encode(msg)) as fileuser:
            fileuser.name = "listusers.txt"
            await tgbot.send_file(
                event.chat_id,
                fileuser,
                force_document=True,
                thumb="userbot/resources/logo.jpg",
                caption="**Total Pengguna Di Bot anda.**",
                allow_cache=False,
                buttons=[
                    (
                        Button.inline("ʙᴀᴄᴋ", data="settings"),
                        Button.inline("ᴄʟᴏsᴇ", data="pmclose"),
                    )
                ],
            )
    else:
        pass


@callback(data=re.compile(b"settings"))
async def botsettings(event):
    await event.delete()
    if event.query.user_id == OWNER_ID:
        await tgbot.send_message(
            event.chat_id,
            message=f"**Halo [{OWNER}](tg://user?id={OWNER_ID})**\n**Apa ada yang bisa saya bantu?**",
            buttons=[
                (Button.inline("sᴇᴛᴛɪɴɢs ᴠᴀʀ", data="apiset"),),
                (
                    Button.inline("ᴘᴍʙᴏᴛ", data="pmbot"),
                    Button.inline("ᴜsᴇʀs", data="users"),
                ),
                (
                    Button.inline("ᴘɪɴɢ", data="pingbot"),
                    Button.inline("ᴜᴘᴛɪᴍᴇ", data="uptimebot"),
                ),
                (Button.inline("ᴄʟᴏsᴇ", data="pmclose"),),
            ],
        )


@callback(data=compile(b"apiset"))
async def apiset(event):
    await event.edit(
        "**Silahkan Pilih API yang ingin anda Setting**",
        buttons=[
            [Button.inline("Remove.bg API", data="rmbg")],
            [Button.inline("DEEP API", data="dapi")],
            [Button.inline("OCR API", data="oapi")],
            [Button.inline("« ʙᴀᴄᴋ", data="settings")],
        ],
    )


@callback(data=compile(b"rmbgapi"))
async def rmbgapi(event):
    await event.delete()
    pru = event.sender_id
    var = "REM_BG_API_KEY"
    name = "Remove.bg API Key"
    async with event.client.conversation(pru) as conv:
        await conv.send_message(get_string("ast_2"))
        response = conv.wait_event(events.NewMessage(chats=pru))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            return await conv.send_message(
                "Cancelled!!",
                buttons=get_back_button("apiset"),
            )
        else:
            await setit(event, var, themssg)
            await conv.send_message(
                f"{name} changed to {themssg}",
                buttons=get_back_button("apiset"),
            )


@callback(data=compile(b"dapi"))
async def rmbgapi(event):
    await event.delete()
    pru = event.sender_id
    var = "DEEP_AI"
    async with event.client.conversation(pru) as conv:
        await conv.send_message("Get Your Deep Api from deepai.org and send here.")
        response = conv.wait_event(events.NewMessage(chats=pru))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            return await conv.send_message(
                "Cancelled!!",
                buttons=get_back_button("apiset"),
            )
        else:
            await setit(event, var, themssg)
            await conv.send_message(
                f"{ALIVE_NAME} changed to {themssg}",
                buttons=get_back_button("apiset"),
            )


@callback(data=compile(b"oaspi"))
async def rmbgapi(event):
    await event.delete()
    pru = event.sender_id
    var = "OCR_SPACE_API_KEY"
    async with event.client.conversation(pru) as conv:
        await conv.send_message("Get Your OCR api from ocr.space Send Send Here.")
        response = conv.wait_event(events.NewMessage(chats=pru))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            return await conv.send_message(
                "Cancelled!!",
                buttons=get_back_button("apiset"),
            )
        else:
            await setit(event, var, themssg)
            await conv.send_message(
                f"{ALIVE_NAME} changed to {themssg}",
                buttons=get_back_button("apiset"),
            )


@callback(data=re.compile(b"pingbot"))
async def _(event):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds
    pin = f"🏓 Pɪɴɢ = {ms} microseconds"
    await event.answer(pin, cache_time=0, alert=True)


@callback(data=re.compile(b"uptimebot"))
async def _(event):
    uptime = await get_readable_time((time.time() - StartTime))
    pin = f"⏱ Uᴘᴛɪᴍᴇ = {uptime}"
    await event.answer(pin, cache_time=0, alert=True)


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
                        \n**Anda dapat menghubungi [{OWNER}](tg://user?id={OWNER_ID}) dari sini.**\
                        \n**Jangan melakukan spam atau anda akan di Banned**\
                        \n\n**Powered by** [UserBot](https://github.com/mrismanaziz/Man-Userbot)"
        buttons = [
            (
                Button.url("ɢʀᴏᴜᴘ", f"https://t.me/{GROUP}"),
                Button.url("ᴄʜᴀɴɴᴇʟ", f"https://t.me/{CHANNEL}"),
            )
        ]
    else:
        start_msg = f"**Halo [{OWNER}](tg://user?id={OWNER_ID})**\
            \n**Apa ada yang bisa saya bantu?**"
        buttons = [
            (Button.inline("sᴇᴛᴛɪɴɢs ᴠᴀʀ", data="apiset"),),
            (
                Button.inline("ᴘᴍʙᴏᴛ", data="pmbot"),
                Button.inline("ᴜsᴇʀs", data="users"),
            ),
            (
                Button.inline("ᴘɪɴɢ", data="pingbot"),
                Button.inline("ᴜᴘᴛɪᴍᴇ", data="uptimebot"),
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
                f"**ERROR:** Saat Pengguna memulai Bot anda.\n`{e}`",
            )

    else:
        await check_bot_started_users(chat, event)


@asst_cmd(pattern="^/id")
async def _(event):
    if event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await tgbot.send_message(
                event.chat_id,
                "**👥 Chat ID:** `{}`\n**🙋‍♂️ From User ID:** `{}`\n**💎 Bot API File ID:** `{}`".format(
                    str(event.chat_id), str(r_msg.sender_id), bot_api_file_id
                ),
            )
        else:
            await tgbot.send_message(
                event.chat_id,
                "**👥 Chat ID:** `{}`\n**🙋‍♂️ From User ID:** `{}`".format(
                    str(event.chat_id), str(r_msg.sender_id)
                ),
            )
    else:
        await tgbot.send_message(
            event.chat_id, "**👥 Chat ID:** `{}`".format(str(event.chat_id))
        )


@asst_cmd(pattern="^/ping$")
async def _(event):
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await tgbot.send_message(
        event.chat_id,
        f"🏓**Pong!**\n`%sms`" % (duration),
    )
