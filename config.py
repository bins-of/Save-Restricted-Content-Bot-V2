# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "26649585"))
API_HASH = getenv("API_HASH", "588a3ea6fd01ae88bd2e10fed7d55b2c")
BOT_TOKEN = getenv("BOT_TOKEN", "7683278474:AAExWYtt_hQ63F4CDYSJhM7LN0o9THEfdFU")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7822720438").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://rohanahamed75:gt4RXJZ1mUtOh4Xv@mmtg.0ong5.mongodb.net/?retryWrites=true&w=majority&appName=mmtg")
LOG_GROUP = getenv("LOG_GROUP", "-1002316472437")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002238603343"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "modijiurl.com")
AD_API = getenv("AD_API", "b8c31803f49c40e6fff829e12c80b8555e9c4202")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
