from os import environ 

class Config:
    API_ID = environ.get("API_ID", "28267656")
    API_HASH = environ.get("API_HASH", "f6a93d5a3896ab581999f9f8733be4be")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8553373827:AAFyXMbHb4qr-X_m0IaW9StP6ftqu8094rg") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://aishopodin_db_user:kDvKtXlI1kFesSDX@cluster0.hs0fmio.mongodb.net/?retryWrites=true&w=majorityappName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6170356257').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
