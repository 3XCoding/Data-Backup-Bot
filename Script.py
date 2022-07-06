class script(object):
    START_TXT = """<b>👋 𝙷𝙸 {},</b>
\n𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈. 𝙾𝚁 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝙼𝙾𝚅𝙸𝙴 𝙽𝙰𝙼𝙴 𝚂𝙴𝙽𝙳 𝙼𝙴😍...\n\n<b>🧑🏻‍💻 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 𝙱𝚈:</b> @VijayAdithyaa"""
    HELP_TXT = """𝙷𝙴𝚈 {}!

<b>𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂.</b>"""
    ABOUT_TXT = """✘ 𝑨𝒃𝒐𝒖𝒕:

<b>‹›</b> <b>𝙼𝚈 𝙽𝙰𝙼𝙴 :</b></b> <a href=http://t.me/HeyNatashaBot>{}</a>
<b>‹›</b> <b>𝙲𝚁𝙴𝙰𝚃𝙾𝚁 :</b> <a href=https://t.me/VijayAdithyaa>ᴀᴅɪᴛʏᴀ ᴀʀ</a>
<b>‹›</b> <b>𝙻𝙸𝙱𝚁𝙰𝚁𝚈 :</b> <a href=https://github.com/pyrogram/pyrogram>Pyrogram</a>
<b>‹›</b> <b>𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 :</b> <a href=https://www.python.com> Python 3</a>
<b>‹›</b> <b>𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴 :</b>  <a href=https://www.mongoDB.com>Mongo DB</a>
<b>‹›</b> <b>𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁 :</b>  <a href=https://heroku.com>Heroku</a>
<b>‹›</b> <b>𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂 :</b> v1.1.46

𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓𝒔:

<b>✧ 𝙰𝚍𝚒𝚝𝚢𝚊 𝙰𝚁</b> × <a href=https://t.me/VijayAdithyaa>ᴀᴅɪᴛʏᴀ ᴀʀ</a>
<b>✧ 𝙴𝚟𝚊 𝙼𝚊𝚛𝚒𝚊</b> × <a href=https://t.me/TeamEvamaria>Eva Maria</a>
<b>✧ 𝙼𝙺𝙽 𝙱𝚘𝚝</b> × <a href=https://t.me/mkn_bots_updates> Mkn Bots</a>"""
    MANUELFILTER_TXT = """✘ 𝑭𝒊𝒍𝒕𝒆𝒓𝒔:

<b>✧</b> 𝙵𝚒𝚕𝚝𝚎𝚛 𝚒𝚜 𝚝𝚑𝚎 𝚏𝚎𝚊𝚝𝚞𝚛𝚎 𝚠𝚎𝚛𝚎 𝚞𝚜𝚎𝚛𝚜 𝚌𝚊𝚗 𝚜𝚎𝚝 𝚊𝚞𝚝𝚘𝚖𝚊𝚝𝚎𝚍 𝚛𝚎𝚙𝚕𝚒𝚎𝚜 𝚏𝚘𝚛 𝚊 𝚙𝚊𝚛𝚝𝚒𝚌𝚞𝚕𝚊𝚛 𝚔𝚎𝚢𝚠𝚘𝚛𝚍 𝚊𝚗𝚍 𝙴𝚟𝚊𝙼𝚊𝚛𝚒𝚊 𝚠𝚒𝚕𝚕 𝚛𝚎𝚜𝚙𝚘𝚗𝚍 𝚠𝚑𝚎𝚗𝚎𝚟𝚎𝚛 𝚊 𝚔𝚎𝚢𝚠𝚘𝚛𝚍 𝚒𝚜 𝚏𝚘𝚞𝚗𝚍 𝚝𝚑𝚎 𝚖𝚎𝚜𝚜𝚊𝚐𝚎.

𝑵𝒐𝒕𝒆:

<b>✧</b> 𝙳𝚊𝚝𝚊 𝙱𝚊𝚌𝚔𝚞𝚙 𝙱𝚘𝚝 𝚜𝚑𝚘𝚞𝚕𝚍 𝚑𝚊𝚟𝚎 𝚊𝚍𝚖𝚒𝚗 𝚙𝚛𝚒𝚟𝚒𝚕𝚕𝚊𝚐𝚎.
<b>✧</b> 𝚘𝚗𝚕𝚢 𝚊𝚍𝚖𝚒𝚗𝚜 𝚌𝚊𝚗 𝚊𝚍𝚍 𝚏𝚒𝚕𝚝𝚎𝚛𝚜 𝚒𝚗 𝚊 𝚌𝚑𝚊𝚝.
<b>✧</b> 𝚊𝚕𝚎𝚛𝚝 𝚋𝚞𝚝𝚝𝚘𝚗𝚜 𝚑𝚊𝚟𝚎 𝚊 𝚕𝚒𝚖𝚒𝚝 𝚘𝚏 𝟼𝟺 𝚌𝚑𝚊𝚛𝚊𝚌𝚝𝚎𝚛𝚜.

𝑪𝒐𝒎𝒎𝒂𝒏𝒅𝒔 𝑨𝒏𝒅 𝑼𝒔𝒂𝒈𝒆:

• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """✘ 𝑩𝒖𝒕𝒕𝒐𝒏𝒔:

<b>¥</b> 𝙳𝚊𝚝𝚊 𝙱𝚊𝚌𝚔𝚞𝚙 𝙱𝚘𝚝 𝚂𝚞𝚙𝚙𝚘𝚛𝚝𝚜 𝚋𝚘𝚝𝚑 𝚞𝚛𝚕 𝚊𝚗𝚍 𝚊𝚕𝚎𝚛𝚝 𝚒𝚗𝚕𝚒𝚗𝚎 𝚋𝚞𝚝𝚝𝚘𝚗𝚜.

𝑵𝒐𝒕𝒆:

<b>✧</b> 𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖 𝚠𝚒𝚕𝚕 𝚗𝚘𝚝 𝚊𝚕𝚕𝚘𝚠𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚜𝚎𝚗𝚍 𝚋𝚞𝚝𝚝𝚘𝚗𝚜 𝚠𝚒𝚝𝚑𝚘𝚞𝚝 𝚊𝚗𝚢 𝚌𝚘𝚗𝚝𝚎𝚗𝚝, 𝚜𝚘 𝚌𝚘𝚗𝚝𝚎𝚗𝚝 𝚒𝚜 𝚖𝚊𝚗𝚍𝚊𝚝𝚘𝚛𝚢.
<b>✧</b> 𝙴𝚟𝚊 𝙼𝚊𝚛𝚒𝚊 𝚜𝚞𝚙𝚙𝚘𝚛𝚝𝚜 𝚋𝚞𝚝𝚝𝚘𝚗𝚜 𝚠𝚒𝚝𝚑 𝚊𝚗𝚢 𝚝𝚎𝚕𝚎𝚐𝚛𝚊𝚖 𝚖𝚎𝚍𝚒𝚊 𝚝𝚢𝚙𝚎.
<b>✧</b> 𝙱𝚞𝚝𝚝𝚘𝚗𝚜 𝚜𝚑𝚘𝚞𝚕𝚍 𝚋𝚎 𝚙𝚛𝚘𝚙𝚎𝚛𝚕𝚢 𝚙𝚊𝚛𝚜𝚎𝚍 𝚊𝚜 𝚖𝚊𝚛𝚔𝚍𝚘𝚠𝚗 𝚏𝚘𝚛𝚖𝚊𝚝

𝑼𝑹𝑳 𝑩𝒖𝒕𝒕𝒐𝒏𝒔:

<b>✧</b> <code>[Button Text](buttonurl:https://t.me/VijayAdithyaa)</code>

𝑨𝒍𝒆𝒓𝒕 𝑩𝒖𝒕𝒕𝒐𝒏𝒔:

<b>✧</b> <code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """✘ 𝑨𝒖𝒕𝒐 𝑭𝒊𝒍𝒕𝒆𝒓:

𝑵𝒐𝒕𝒆:

<b>✧</b> 𝙼𝚊𝚔𝚎 𝚖𝚎 𝚝𝚑𝚎 𝚊𝚍𝚖𝚒𝚗 𝚘𝚏 𝚢𝚘𝚞𝚛 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 𝚒𝚏 𝚒𝚝'𝚜 𝚙𝚛𝚒𝚟𝚊𝚝𝚎.
<b>✧</b> 𝚖𝚊𝚔𝚎 𝚜𝚞𝚛𝚎 𝚝𝚑𝚊𝚝 𝚢𝚘𝚞𝚛 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 𝚍𝚘𝚎𝚜 𝚗𝚘𝚝 𝚌𝚘𝚗𝚝𝚊𝚒𝚗𝚜 𝚌𝚊𝚖𝚛𝚒𝚙𝚜, 𝚙𝚘𝚛𝚗 𝚊𝚗𝚍 𝚏𝚊𝚔𝚎 𝚏𝚒𝚕𝚎𝚜.
<b>✧</b> 𝙵𝚘𝚛𝚠𝚊𝚛𝚍 𝚝𝚑𝚎 𝚕𝚊𝚜𝚝 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚝𝚘 𝚖𝚎 𝚠𝚒𝚝𝚑 𝚚𝚞𝚘𝚝𝚎𝚜.
𝙸'𝚕𝚕 𝚊𝚍𝚍 𝚊𝚕𝚕 𝚝𝚑𝚎 𝚏𝚒𝚕𝚎𝚜 𝚒𝚗 𝚝𝚑𝚊𝚝 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 𝚝𝚘 𝚖𝚢 𝚍𝚋."""
    CONNECTION_TXT = """✘ 𝑪𝒐𝒏𝒏𝒆𝒄𝒕𝒊𝒐𝒏𝒔:

<b>✧</b> 𝚄𝚜𝚎𝚍 𝚝𝚘 𝚌𝚘𝚗𝚗𝚎𝚌𝚝 𝚋𝚘𝚝 𝚝𝚘 𝙿𝙼 𝚏𝚘𝚛 𝚖𝚊𝚗𝚊𝚐𝚒𝚗𝚐 𝚏𝚒𝚕𝚝𝚎𝚛𝚜 
<b>✧</b> 𝚒𝚝 𝚑𝚎𝚕𝚙𝚜 𝚝𝚘 𝚊𝚟𝚘𝚒𝚍 𝚜𝚙𝚊𝚖𝚖𝚒𝚗𝚐 𝚒𝚗 𝚐𝚛𝚘𝚞𝚙𝚜.

𝑵𝒐𝒕𝒆:

<b>✧</b> 𝙾𝚗𝚕𝚢 𝚊𝚍𝚖𝚒𝚗𝚜 𝚌𝚊𝚗 𝚊𝚍𝚍 𝚊 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚘𝚗.
<b>✧</b> 𝚂𝚎𝚗𝚍 <𝚌𝚘𝚍𝚎>/𝚌𝚘𝚗𝚗𝚎𝚌𝚝 𝚏𝚘𝚛 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚒𝚗𝚐 𝚖𝚎 𝚝𝚘 𝚞𝚛 𝙿𝙼

𝑪𝒐𝒎𝒎𝒂𝒏𝒅𝒔 𝑨𝒏𝒅 𝑼𝒔𝒂𝒈𝒆:

• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """✘ 𝑬𝒙𝒕𝒓𝒂 𝑴𝒐𝒅𝒖𝒍𝒆𝒔:

𝑵𝒐𝒕𝒆:

<b>✧</b> 𝚃𝚑𝚎𝚜𝚎 𝚊𝚛𝚎 𝚝𝚑𝚎 𝚎𝚡𝚝𝚛𝚊 𝚏𝚎𝚊𝚝𝚞𝚛𝚎𝚜 𝚘𝚏 𝙳𝚊𝚝𝚊 𝙱𝚊𝚌𝚔𝚞𝚙 𝙱𝚘𝚝
𝑪𝒐𝒎𝒎𝒂𝒏𝒅𝒔 𝑨𝒏𝒅 𝑼𝒔𝒂𝒈𝒆:

• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /whois - <code>give a user full details</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """✘ 𝑶𝒘𝒏𝒆𝒓 𝑴𝒐𝒅𝒔:

𝑵𝒐𝒕𝒆:

<b>✧</b> 𝚃𝚑𝚒𝚜 𝚖𝚘𝚍𝚞𝚕𝚎 𝚘𝚗𝚕𝚢 𝚠𝚘𝚛𝚔𝚜 𝚏𝚘𝚛 𝚖𝚢 𝚊𝚍𝚖𝚒𝚗𝚜

𝑪𝒐𝒎𝒎𝒂𝒏𝒅𝒔 𝑨𝒏𝒅 𝑼𝒔𝒂𝒈𝒆:

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
    STATUS_TXT = """✘ 𝑫𝒂𝒕𝒂𝒃𝒂𝒔𝒆:

<b>‹› 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂 :</b> {}
<b>‹› 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂 :</b> {}
<b>‹› 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂 :</b> {}
<b>‹› 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴 :</b> {}
<b>‹› 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴 :</b> {}"""
    FOND_TXT = """✘ 𝑭𝒐𝒏𝒕 𝑪𝒐𝒑𝒚 & 𝑷𝒍𝒆𝒂𝒔𝒆:

<b>✧</b> 𝙵𝙾𝙽𝚃 𝙸𝚂 𝙰 𝙼𝙾𝙳𝚄𝙻𝙴 𝙵𝙾𝚁 𝙼𝙰𝙺𝙴 𝚈𝙾𝚄𝚁 𝚃𝙴𝚇𝚃 𝚂𝚃𝚈𝙻𝙸𝚂𝙷.
<b>✧</b> 𝙵𝙾𝚁 𝚄𝚂𝙴 𝚃𝙷𝙰𝚃 𝙵𝙴𝚄𝚃𝚄𝚁𝙴 𝚃𝚈𝙿𝙴 /font <your text> 𝚃𝙷𝙴𝙽 𝚈𝙾𝚄𝚁 𝚃𝙴𝚇𝚃 𝙸𝚂 𝚁𝙴𝙰𝙳𝚈."""
    TTS_TXT = """✘ 𝑻𝒆𝒙𝒕 𝑻𝒐 𝑺𝒑𝒆𝒆𝒄𝒉:

<b>✧</b> Translate text to speech

𝑪𝒐𝒎𝒎𝒂𝒏𝒅𝒔 𝑨𝒏𝒅 𝑼𝒔𝒂𝒈𝒆:

• /tts <text> : convert text to speech

𝑵𝒐𝒕𝒆:

<b>✧</b> 𝙸𝙼𝙳𝚋 𝚜𝚑𝚘𝚞𝚕𝚍 𝚑𝚊𝚟𝚎 𝚊𝚍𝚖𝚒𝚗 𝚙𝚛𝚒𝚟𝚒𝚕𝚕𝚊𝚐𝚎.
<b>✧</b> 𝚃𝚑𝚎𝚜𝚎 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜 𝚠𝚘𝚛𝚔𝚜 𝚘𝚗 𝚋𝚘𝚝𝚑 𝚙𝚖 𝚊𝚗𝚍 𝚐𝚛𝚘𝚞𝚙.
<b>✧</b> 𝙸𝙼𝙳𝚋 𝚌𝚊𝚗 𝚝𝚛𝚊𝚗𝚜𝚕𝚊𝚝𝚎 𝚝𝚎𝚡𝚝𝚜 𝚝𝚘 𝟸𝟶𝟶+ 𝚕𝚊𝚗𝚐𝚞𝚊𝚐𝚎𝚜."""
    TELE_TXT = """✘ 𝑻𝒆𝒍𝒆𝒈𝒓𝒂𝒑𝒉:

<b>✧</b> 𝙳𝚘 𝚊𝚜 𝚢𝚘𝚞 𝚠𝚒𝚜𝚑 𝚠𝚒𝚝𝚑 𝚝𝚎𝚕𝚎𝚐𝚛𝚊.𝚙𝚑 𝚖𝚘𝚍𝚞𝚕𝚎.

𝑪𝒐𝒎𝒎𝒂𝒏𝒅𝒔 𝑨𝒏𝒅 𝑼𝒔𝒂𝒈𝒆:

• /telegraph - Send me Picture or Video Under (5MB)

𝑵𝒐𝒕𝒆:

<b>✧</b> 𝚃𝚑𝚒𝚜 𝙲𝚘𝚖𝚖𝚊𝚗𝚍 𝙸𝚜 𝙰𝚟𝚊𝚒𝚕𝚊𝚋𝚕𝚎 𝚒𝚗 𝚐𝚘𝚞𝚙𝚜 𝚊𝚗𝚍 𝙿𝙼𝚜
<b>✧</b> 𝚃𝚑𝚒𝚜 𝙲𝚘𝚖𝚖𝚊𝚗𝚍 𝙲𝚊𝚗 𝚋𝚎 𝚞𝚜𝚎𝚍 𝚋𝚢 𝚎𝚟𝚎𝚛𝚢𝚘𝚗𝚎"""
    ABOOK_TXT = """✘ 𝑨𝒖𝒅𝒊𝒐𝑩𝒐𝒐𝒌:

𝑵𝒐𝒕𝒆:

𝚈𝚘𝚞 𝚌𝚊𝚗 𝚌𝚘𝚗𝚟𝚎𝚛𝚝 𝚊 𝙿𝙳𝙵 𝚏𝚒𝚕𝚎 𝚝𝚘 𝚊 𝚊𝚞𝚍𝚒𝚘 𝚏𝚒𝚕𝚎 𝚠𝚒𝚝𝚑 𝚝𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍.

𝑪𝒐𝒎𝒎𝒂𝒏𝒅𝒔 𝑨𝒏𝒅 𝑼𝒔𝒂𝒈𝒆:

• /audiobook: 𝖱𝖾𝗉𝗅𝗒 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗍𝗈 𝖺𝗇𝗒 𝖯𝖣𝖥 𝗍𝗈 𝗀𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝗍𝗁𝖾 𝖺𝗎𝖽𝗂𝗈"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewBotUser:
ID - <code>{}</code>
Name - {}
"""

MELCOW_ENG = """ <b>👋 𝙷𝙸 {user}.</b>\n🥳 Welcome To {chat}!\n\n<b>❯ 𝙽𝙰𝙼𝙴 :</b> {user}\n<b>❯ 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙸𝙳 :</b> {user_id}\n<b>❯ 𝙳𝙰𝚃𝙰 𝙲𝙴𝙽𝚃𝚁𝙴:</b> {user_dc}\n<b>❯ 𝚄𝚂𝙴𝚁 𝙿𝚁𝙾𝙵𝙸𝙻𝙴:</b> <a href='tg://user?id={user}'><b>Click Here</b></a>\n🎉 Thank you for join {chat_name}\n\n<b>🧑🏻‍💻 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 𝙱𝚈:</b> @VijayAdithyaa"""
