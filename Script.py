class script(object):
    START_TXT = """<b>𝙷𝙸 {},</b>
\n𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 😍\n\n<b>𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈:</b> @VijayAdithyaa"""
    HELP_TXT = """𝙷𝙴𝚈 {}!

<b>𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂.</b>"""
    ABOUT_TXT = """💡 𝑨𝒃𝒐𝒖𝒕:

<b>‹›</b> <b>𝙼𝚈 𝙽𝙰𝙼𝙴 :</b></b> {}
<b>‹›</b> <b>𝙲𝚁𝙴𝙰𝚃𝙾𝚁 :</b> <a href=https://t.me/VijayAdithyaa>ᴀᴅɪᴛʏᴀ ᴀʀ</a>
<b>‹›</b> <b>𝙻𝙸𝙱𝚁𝙰𝚁𝚈 :</b> Pyrogram
<b>‹›</b> <b>𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 :</b> Python 3
<b>‹›</b> <b>𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴 :</b> Mongo DB
<b>‹›</b> <b>𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁 :</b> Heroku
<b>‹›</b> <b>𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂 :</b> v1.0.25"""
    SOURCE_TXT = """🔆 𝑺𝒐𝒖𝒓𝒄𝒆:

𝑵𝒐𝒕𝒆:
<b>×</b> Data Backup Bot is a open source project. 
<b>×</b> Source : <a href=https://github.com/HeyAdithya/Data-Backup-Bot>GitHub+Adithya</a>

𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓𝒔:
<b>×</b> <a href=https://t.me/VijayAdithyaa>ᴀᴅɪᴛʏᴀ ᴀʀ</a>
<b>×</b> <a href=https://t.me/TeamEvamaria>Eva Maria</a>"""
    MANUELFILTER_TXT = """𝑭𝒊𝒍𝒕𝒆𝒓𝒔:
<b>×</b> Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

𝑵𝒐𝒕𝒆:
<b>×</b> Data Backup Bot should have admin privillage.
<b>×</b> only admins can add filters in a chat.
<b>×</b> alert buttons have a limit of 64 characters.

𝑪𝒐𝒎𝒎𝒂𝒏𝒅𝒔 𝑨𝒏𝒅 𝑼𝒔𝒂𝒈𝒆:
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

𝑪𝒐𝒎𝒎𝒂𝒏𝒅𝒔 𝑨𝒏𝒅 𝑼𝒔𝒂𝒈𝒆:
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """𝑬𝒙𝒕𝒓𝒂 𝑴𝒐𝒅𝒖𝒍𝒆𝒔:

𝑵𝒐𝒕𝒆:
<b>×</b> These are the extra features of Data Backup Bot

𝑪𝒐𝒎𝒎𝒂𝒏𝒅𝒔 𝑨𝒏𝒅 𝑼𝒔𝒂𝒈𝒆:
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /whois - <code>give a user full details</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """𝑶𝒘𝒏𝒆𝒓 𝑴𝒐𝒅𝒔:

𝑵𝒐𝒕𝒆:
<b>×</b> This module only works for my admins

𝑪𝒐𝒎𝒎𝒂𝒏𝒅𝒔 𝑨𝒏𝒅 𝑼𝒔𝒂𝒈𝒆:
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /telegraph - <code>Send me Picture or Vide Under (5MB)</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """🖱 𝑫𝒂𝒕𝒂𝒃𝒂𝒔𝒆:

<b>‹› 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂 :</b> {}
<b>‹› 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂 :</b> {}
<b>‹› 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂 :</b> {}
<b>‹› 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴 :</b> {}
<b>‹› 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴 :</b> {}"""
    FOND_TXT = """𝑭𝒐𝒏𝒕 𝑪𝒐𝒑𝒚 & 𝑷𝒍𝒆𝒂𝒔𝒆:

<b>×</b> 𝙵𝙾𝙽𝚃 𝙸𝚂 𝙰 𝙼𝙾𝙳𝚄𝙻𝙴 𝙵𝙾𝚁 𝙼𝙰𝙺𝙴 𝚈𝙾𝚄𝚁 𝚃𝙴𝚇𝚃 𝚂𝚃𝚈𝙻𝙸𝚂𝙷.
𝙵𝙾𝚁 𝚄𝚂𝙴 𝚃𝙷𝙰𝚃 𝙵𝙴𝚄𝚃𝚄𝚁𝙴 𝚃𝚈𝙿𝙴 /font <your text> 𝚃𝙷𝙴𝙽 𝚈𝙾𝚄𝚁 𝚃𝙴𝚇𝚃 𝙸𝚂 𝚁𝙴𝙰𝙳𝚈."""
    LOG_TEXT_G = """#NewGroup

Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewBotUser:

ID - <code>{}</code>
Name - {}
"""
