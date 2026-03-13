# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "28642558"))
    API_HASH = getenv("API_HASH", "8ebf6f5403d9494a94f1ee1330027ed8")
    BOT_TOKEN = getenv("BOT_TOKEN", "8604718668:AAFXqMcI0zeca6ksfxL-msF7MNmNkpBioTY")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1002287523304")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "5252260061").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://premashilarana681_db_user:GMucI9xhkmvNUOX2@cluster0.8mlerkv.mongodb.net/?appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
