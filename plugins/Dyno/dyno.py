import os
import math
import time
from info import ADMINS
import heroku3
import requests
from pyrogram import Client, filters
from databasevs.users_chats_db import db

#=====================================================
BOT_START_TIME = time.time()
CMD = ['.', '/']
HEROKU_API_KEY = (os.environ.get("HEROKU_API_KEY", ""))
#=====================================================

@Client.on_message(filters.group | filters.private & filters.user(ADMINS) & filters.command("dyno", CMD))         
async def bot_status_cmd(client,message):
    if HEROKU_API_KEY:
        try:
            server = heroku3.from_key(HEROKU_API_KEY)

            user_agent = (
                'Mozilla/5.0 (Linux; Android 10; SM-G975F) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/80.0.3987.149 Mobile Safari/537.36'
            )
            accountid = server.account().id
            headers = {
            'User-Agent': user_agent,
            'Authorization': f'Bearer {HEROKU_API_KEY}',
            'Accept': 'application/vnd.heroku+json; version=3.account-quotas',
            }

            path = "/accounts/" + accountid + "/actions/get-quota"

            request = requests.get("https://api.heroku.com" + path, headers=headers)

            if request.status_code == 200:
                result = request.json()

                total_quota = result['account_quota']
                quota_used = result['quota_used']

                quota_left = total_quota - quota_used
                
                total = math.floor(total_quota/3600)
                used = math.floor(quota_used/3600)
                hours = math.floor(quota_left/3600)
                minutes = math.floor(quota_left/60 % 60)
                days = math.floor(hours/24)

                usedperc = math.floor(quota_used / total_quota * 100)
                leftperc = math.floor(quota_left / total_quota * 100)

#---------text--------🔥

                quota_details = f"""
𝑩𝒐𝒕 𝑺𝒆𝒓𝒗𝒆𝒓:

<b>✧ 𝚃𝙾𝚃𝙰𝙻 𝙳𝚈𝙽𝙾 :</b> {total} ʜᴏᴜʀꜱ ꜰʀᴇᴇ ᴅʏɴᴏ!
 
<b>✧ 𝙳𝚈𝙽𝙾 𝚄𝚂𝙴𝙳 :</b> {used} ʜᴏᴜʀꜱ = {usedperc}%
        
<b>✧ 𝙳𝚈𝙽𝙾 𝚁𝙴𝙼𝙰𝙸𝙽𝙸𝙽𝙶 :</b> {hours} ʜᴏᴜʀꜱ = {leftperc}%
        
<b>✧ 𝙰𝙿𝙿𝚁𝙾𝚇𝙸𝙼𝙰𝚃𝙴 𝙳𝙰𝚈𝚂 :</b> {days} ᴅᴀʏꜱ ʟɪꜰᴇ!"""

#----------end---------💯

            else:
                quota_details = ""
        except:
            print("Check your Heroku API key")
            quota_details = ""
    else:
        quota_details = ""

    uptime = time.strftime("%Hh %Mm %Ss", time.gmtime(time.time() - BOT_START_TIME))

    try:
        t, u, f = shutil.disk_usage(".")
        total = humanbytes(t)
        used = humanbytes(u)
        free = humanbytes(f)

        disk = "\n**𝑫𝒊𝒔𝒌 𝑫𝒆𝒕𝒂𝒊𝒍𝒔**\n\n" \
            f"✧ USED  :  {used} / {total}\n" \
            f"✧ FREE  :  {free}\n\n"
    except:
        disk = ""

    await message.reply_text(
        "<u>𝑪𝒖𝒓𝒓𝒆𝒏𝒕 𝑺𝒕𝒂𝒕𝒖𝒔 𝑶𝒇 𝒀𝒐𝒖𝒓 𝑩𝒐𝒕:</u>\n\n"
        "𝑫𝒂𝒕𝒂 𝑪𝒆𝒏𝒕𝒆𝒓 𝑺𝒕𝒂𝒕𝒖𝒔:\n\n"
        f"<b>✧ 𝙱𝙾𝚃 𝚄𝙿𝚃𝙸𝙼𝙴 :</b> {uptime}\n"
        f"{quota_details}"
        f"{disk}",
        quote=True,
        parse_mode="html"
    )
