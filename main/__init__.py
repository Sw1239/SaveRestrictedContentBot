#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", "34163601")
API_HASH = config("API_HASH", "99f1dff24a940e88c18247e91e7eef06")
BOT_TOKEN = config("BOT_TOKEN", "8272323148:AAHTXlf9Qz5IuxBg-e8GPJco3Ixi07IrqBo")
SESSION = config("SESSION", "BQIJS5EAYGNjpQCTu79AqYCm-M8hPfTEByk6yjJjtaZ8eSUk3y_Dmwdyr2fV67WnIuvxu4PiRLIeYDO0q9Vc4bvt15vLJOs0JmThTPBwYLdSgRvWpcx1nlvxW7J0LGQsgACfFeWKT7zvSyH9dLRa7tDvS8TNp4fKE4nV3c-Zsdt6UXBHmLbLFxz9xmHqsR8i-IaXoxD9xf1Qc1Ad7rx9PbkpelRLO48txpTeSKsnTCCNXmxm86nyKkHfUuPneX3PgzTXat1g9U3mRj1aZALPpAR9gfVnIUNWRIW67EMAXbZjVXb3eqgnfhTK_0tIdVmyCXJEw2Na_2kvQwEF4_OwlayyCIyzhQAAAAGcVd_kAA")
FORCESUB = config("FORCESUB", "my saved")
AUTH = config("AUTH", "dummy_bots")

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
