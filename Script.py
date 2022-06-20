class script(object):
    START_TXT = """<b>𝙷𝙸 {},</b>
\n𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 😍\n\n<b>𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈:</b> @VijayAdithyaa"""
    HELP_TXT = """𝙷𝙴𝚈 {}

<b>𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂.</b>"""
    ABOUT_TXT = """⤷ 𝑨𝒃𝒐𝒖𝒕:
✯ <b>𝙼𝚈 𝙽𝙰𝙼𝙴:</b> {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/VijayAdithyaa>ᴀᴅɪᴛʏᴀ ᴀʀ</a>
✯ <b>𝙻𝙸𝙱𝚁𝙰𝚁𝚈:</b> 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ <b>𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴:</b> 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ <b>𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴:</b> 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ <b>𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁:</b> 𝙷𝙴𝚁𝙾𝙺𝚄
✯ <b>𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂:</b> v1.0.2"""
    SOURCE_TXT = """𝑵𝒐𝒕𝒆:
➜ Data Backup Bot is a open source project. 
➜ Source : <a href=https://github.com/HeyAdithya/Data-Backup-Bot>GitHub+Adithya</a>

<b>ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ:</b>
➜ <a href=https://t.me/VijayAdithyaa>ᴀᴅɪᴛʏᴀ ᴀʀ</a>
➜ <a href=https://t.me/TeamEvamaria>Eva Maria</a>"""
    MANUELFILTER_TXT = """𝑭𝒊𝒍𝒕𝒆𝒓𝒔:
<b>×</b> Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

𝑵𝒐𝒕𝒆:
<b>×</b> Data Backup Bot should have admin privillage.
<b>×</b> only admins can add filters in a chat.
<b>×</b> alert buttons have a limit of 64 characters.

<b>𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜 𝙰𝚗𝚍 𝚄𝚜𝚊𝚐𝚎:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """𝑩𝒖𝒕𝒕𝒐𝒏𝒔:
<b>×</b> Data Backup Bot Supports both url and alert inline buttons.

𝑵𝒐𝒕𝒆:
<b>×</b> Telegram will not allows you to send buttons without any content, so content is mandatory.
<b>×</b> Eva Maria supports buttons with any telegram media type.
<b>×</b> Buttons should be properly parsed as markdown format

𝑼𝑹𝑳 𝑩𝒖𝒕𝒕𝒐𝒏𝒔:
<b>×</b> <code>[Button Text](buttonurl:https://t.me/VijayAdithyaa)</code>

𝑨𝒍𝒆𝒓𝒕 𝑩𝒖𝒕𝒕𝒐𝒏𝒔:
<b>×</b> <code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """𝑨𝒖𝒕𝒐 𝑭𝒊𝒍𝒕𝒆𝒓:

𝑵𝒐𝒕𝒆:
<b>×</b> Make me the admin of your channel if it's private.
<b>×</b> make sure that your channel does not contains camrips, porn and fake files.
<b>×</b> Forward the last message to me with quotes.
   I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """𝑪𝒐𝒏𝒏𝒆𝒄𝒕𝒊𝒐𝒏𝒔:
<b>×</b> Used to connect bot to PM for managing filters 
<b>×</b> it helps to avoid spamming in groups.

𝑵𝒐𝒕𝒆:
<b>×</b> Only admins can add a connection.
<b>×</b> Send <code>/connect</code> for connecting me to ur PM

<b>𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜 𝙰𝚗𝚍 𝚄𝚜𝚊𝚐𝚎:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """𝑬𝒙𝒕𝒓𝒂 𝑴𝒐𝒅𝒖𝒍𝒆𝒔:

𝑵𝒐𝒕𝒆:
<b>×</b> These are the extra features of Data Backup Bot

<b>𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜 𝙰𝚗𝚍 𝚄𝚜𝚊𝚐𝚎:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """𝑨𝒅𝒎𝒊𝒏 𝑴𝒐𝒅𝒔:

𝑵𝒐𝒕𝒆:
<b>×</b> This module only works for my admins

<b>𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜 𝙰𝚗𝚍 𝚄𝚜𝚊𝚐𝚎:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """🖱 𝑫𝒂𝒕𝒂𝒃𝒂𝒔𝒆:

<b>‹› 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂:</b> <code>{}</code>
<b>‹› 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂:</b> <code>{}</code>
<b>‹› 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂:</b> <code>{}</code>
<b>‹› 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴:</b> <code>{}</code>
<b>‹› 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴:</b> <code>{}</code>"""
    LOG_TEXT_G = """New Group

Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """Bot New User:

ID - <code>{}</code>
Name - {}
"""
