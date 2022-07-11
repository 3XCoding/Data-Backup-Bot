import asyncio
import os
from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from databasevs.connections_mdb import active_connection, all_connections, delete_connection, if_active, make_active, make_inactive, \
    make_inactive
from info import IMDB_TEMPLATE, IMDB_DELET_TIME
from utils import extract_user, get_file_id, get_poster, last_online
import time
from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

@Client.on_message(filters.command('id'))
async def showid(client, message):
    chat_type = message.chat.type
    if chat_type == "private":
        user_id = message.chat.id
        first = message.from_user.first_name
        last = message.from_user.last_name or ""
        username = message.from_user.username
        dc_id = message.from_user.dc_id or ""
        await message.reply_text(
            f"<b>❯ 𝙵𝙸𝚁𝚂𝚃 𝙽𝙰𝙼𝙴:</b> {first}\n<b>❯ 𝙻𝙰𝚂𝚃 𝙽𝙰𝙼𝙴:</b> {last}\n<b>❯ 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴:</b> {username}\n<b>❯ 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙸𝙳:</b> <code>{user_id}</code>\n<b>❯ 𝙳𝙰𝚃𝙰 𝙲𝙴𝙽𝚃𝚁𝙴:</b> <code>{dc_id}</code>",
            quote=True
        )

    elif chat_type in ["group", "supergroup"]:
        _id = ""
        _id += (
            "<b>❯ 𝙶𝚁𝙾𝚄𝙿 𝙸𝙳:</b>: "
            f"<code>{message.chat.id}</code>\n"
        )
        if message.reply_to_message:
            _id += (
                "<b>❯ 𝚄𝚂𝙴𝚁 𝙸𝙳:</b> "
                f"<code>{message.from_user.id if message.from_user else 'Anonymous'}</code>\n"
                "<b>❯ 𝚁𝙴𝙿𝙻𝙸𝙴𝙳 𝙸𝙳:</b> "
                f"<code>{message.reply_to_message.from_user.id if message.reply_to_message.from_user else 'Anonymous'}</code>\n"
            )
            file_info = get_file_id(message.reply_to_message)
        else:
            _id += (
                "<b>➲ User ID</b>: "
                f"<code>{message.from_user.id if message.from_user else 'Anonymous'}</code>\n"
            )
            file_info = get_file_id(message)
        if file_info:
            _id += (
                f"<b>{file_info.message_type}</b>: "
                f"<code>{file_info.file_id}</code>\n"
            )
        await message.reply_text(
            _id,
            quote=True
        )

@Client.on_message(filters.command(["info"]))
async def who_is(client, message):
    # https://github.com/SpEcHiDe/PyroGramBot/blob/master/pyrobot/plugins/admemes/whois.py#L19
    status_message = await message.reply_text(
        "`Fetching user info...`"
    )
    await status_message.edit(
        "`Processing user info...`"
    )
    from_user = None
    from_user_id, _ = extract_user(message)
    try:
        from_user = await client.get_users(from_user_id)
    except Exception as error:
        await status_message.edit(str(error))
        return
    if from_user is None:
        return await status_message.edit("no valid user_id / message specified")
    message_out_str = ""
    message_out_str += f"<b>❯ 𝙵𝙸𝚁𝚂𝚃 𝙽𝙰𝙼𝙴:</b> {from_user.first_name}\n"
    last_name = from_user.last_name or "<b>None</b>"
    message_out_str += f"<b>❯ 𝙻𝙰𝚂𝚃 𝙽𝙰𝙼𝙴:</b> {last_name}\n"
    message_out_str += f"<b>❯ 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙸𝙳:</b> <code>{from_user.id}</code>\n"
    username = from_user.username or "<b>None</b>"
    dc_id = from_user.dc_id or "[User Doesn't Have A Valid DP]"
    message_out_str += f"<b>❯ 𝙳𝙰𝚃𝙰 𝙲𝙴𝙽𝚃𝚁𝙴:</b> <code>{dc_id}</code>\n"
    message_out_str += f"<b>❯ 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴:</b> @{username}\n"
    message_out_str += f"<b>❯ 𝚄𝚂𝙴𝚁 𝙿𝚁𝙾𝙵𝙸𝙻𝙴:</b> <a href='tg://user?id={from_user.id}'><b>Click Here</b></a>\n"
    if message.chat.type in (("supergroup", "channel")):
        try:
            chat_member_p = await message.chat.get_member(from_user.id)
            joined_date = datetime.fromtimestamp(
                chat_member_p.joined_date or time.time()
            ).strftime("%Y.%m.%d %H:%M:%S")
            message_out_str += (
                "<b>❯ 𝙶𝚁𝙾𝚄𝙿 𝙹𝙾𝙸𝙽 𝙾𝙽:</b> <code>"
                f"{joined_date}"
                "</code>\n"
            )
        except UserNotParticipant:
            pass
    chat_photo = from_user.photo
    if chat_photo:
        local_user_photo = await client.download_media(
            message=chat_photo.big_file_id
        )
        buttons = [[
            InlineKeyboardButton('🗑 𝙲𝙻𝙾𝚂𝙴', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=local_user_photo,
            quote=True,
            reply_markup=reply_markup,
            caption=message_out_str,
            parse_mode="html",
            disable_notification=True
        )
        os.remove(local_user_photo)
    else:
        buttons = [[
            InlineKeyboardButton('🗑 𝙲𝙻𝙾𝚂𝙴', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(
            text=message_out_str,
            reply_markup=reply_markup,
            quote=True,
            parse_mode="html",
            disable_notification=True
        )
    await status_message.delete()

@Client.on_message(filters.command(["imdb", 'search']))
async def imdb_search(client, message):
    if ' ' in message.text:
        k = await message.reply('Searching ImDB')
        r, title = message.text.split(None, 1)
        movies = await get_poster(title, bulk=True)
        if not movies:
            return await message.reply("𝙽𝙾 𝚁𝙴𝚂𝚄𝙻𝚃𝚂 𝙵𝙾𝚄𝙽𝙳")
        btn = [
            [
                InlineKeyboardButton(
                    text=f"{movie.get('title')} - {movie.get('year')}",
                    callback_data=f"imdb#{movie.movieID}",
                )
            ]
            for movie in movies
        ]
        await k.edit('𝙷𝙴𝚁𝙴 𝙸𝚂 𝚆𝙷𝙰𝚃 𝙸 𝙵𝙾𝚄𝙽𝙳 𝙾𝙽 𝙸𝙼𝙳𝙱', reply_markup=InlineKeyboardMarkup(btn))
        await asyncio.sleep(IMDB_DELET_TIME)
        await k.delete()
    else:
        await message.reply('𝙶𝙸𝚅𝙴 𝙼𝙴 𝙰 𝙼𝙾𝚅𝙸𝙴 / 𝚂𝙴𝚁𝙸𝙴𝚂 𝙽𝙰𝙼𝙴')
        await asyncio.sleep(3)
        await k.delete()

@Client.on_callback_query(filters.regex('^imdb'))
async def imdb_callback(bot: Client, quer_y: CallbackQuery):
    i, movie = quer_y.data.split('#')
    imdb = await get_poster(query=movie, id=True)
    btn = [
            [
                InlineKeyboardButton(
                    text=f"{imdb.get('title')}",
                    url=imdb['url'],
                )
            ]
        ]
    message = quer_y.message.reply_to_message or quer_y.message
    if imdb:
        caption= IMDB_TEMPLATE.format(
            query = imdb['title'],
            title = imdb['title'],
            votes = imdb['votes'],
            reviews = imdb['reviews'],
            aka = imdb["aka"],
            seasons = imdb["seasons"],
            box_office = imdb['box_office'],
            localized_title = imdb['localized_title'],
            kind = imdb['kind'],
            imdb_id = imdb["imdb_id"],
            cast = imdb["cast"],
            runtime = imdb["runtime"],
            countries = imdb["countries"],
            certificates = imdb["certificates"],
            languages = imdb["languages"],
            director = imdb["director"],
            writer = imdb["writer"],
            producer = imdb["producer"],
            composer = imdb["composer"],
            cinematographer = imdb["cinematographer"],
            music_team = imdb["music_team"],
            distributors = imdb["distributors"],
            release_date = imdb['release_date'],
            year = imdb['year'],
            genres = imdb['genres'],
            poster = imdb['poster'],
            plot = imdb['plot'],
            rating = imdb['rating'],
            url = imdb['url'],
            **locals()
        )
    else:
        caption = "No Results"
    if imdb.get('poster'):
        try:
            hehe = await message.reply_photo(photo=imdb.get('poster'), caption=caption, reply_markup=InlineKeyboardMarkup(btn))
            await asyncio.sleep(IMDB_DELET_TIME)
            await hehe.delete()
            await message.reply_text(text=f"", disable_notification = True)
        except (MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty):
            pic = imdb.get('poster')
            poster = pic.replace('.jpg', "._V1_UX360.jpg")
            hmm = await message.reply_photo(photo=poster, caption=caption, reply_markup=InlineKeyboardMarkup(btn))
            await asyncio.sleep(IMDB_DELET_TIME)
            await hmm.edit_text(text=f"", disable_notification = True)
        except Exception as e:
            logger.exception(e)
            fek = await message.reply_photo(photo="", caption=caption, reply_markup=InlineKeyboardMarkup(btn))
            await asyncio.sleep(IMDB_DELET_TIME)
            await fek.edit_text(text=f"")
    else:
        fuk = await message.reply_photo(photo="", caption=caption, reply_markup=InlineKeyboardMarkup(btn))
        await asyncio.sleep(IMDB_DELET_TIME)
        await fuk.delete()




