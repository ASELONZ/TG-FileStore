# (c) @PredatorHackerzZ || @TeleRoidGroup

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "0"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-100"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1445283714"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File.I can Work In Channel too Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸 **Mʏ Nᴀᴍᴇ:** [Dᴇғᴇɴᴅᴇʀ](https://t.me/{BOT_USERNAME})

├🔸 **Oᴡɴᴇʀ:** [@ANKIT3690](https://t.me/ANKIT3690) 
├🔸 **Oᴡɴᴇʀ:** [@Saurav3BV6SA9LLElon7Musk](https://t.me/Saurav3BV6SA9LLElon7Musk) 
│
├🔹 **Gʀᴏᴜᴘ:** [𝓽ꫝꫀ ᥴ𝘳ꫀꪖ𝓽ꪮ𝘳 ꪮᠻ ꪖꪶꪶ](https://t.me/thewarriorsreal )
│
├🔸 **Cᕼᴀɴɴᴇʟ:** [𝐃𝐄𝐅𝐄𝐍𝐃𝐄𝐑 𝐎𝐅 𝐓𝐇𝐄 𝐌𝐔𝐋𝐓𝐈𝐕𝐄𝐑𝐒𝐄](https://t.me/defenderofthemultiverse)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
├🔸 **Oᴡɴᴇʀ:** [@ANKIT3690](https://t.me/ANKIT3690) 
├🔸 **Oᴡɴᴇʀ:** [@Saurav3BV6SA9LLElon7Musk](https://t.me/Saurav3BV6SA9LLElon7Musk)

This Bot is only for file sharing made by my creator.
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.
I provide permanent files shareable link.
Credits:[UNKNOWN]((tg://user?id={}))
"""
