# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "23621595")
    API_HASH = environ.get("API_HASH", "de904be2b4cd4efe2ea728ded17ca77d")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7692381687:AAEqmbwW1I1zA8aDUuPb0kcY2GkiTJVfu3E") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1249672673').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://graph.org/file/e223aea8aca83e99162bb.jpg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://mongodb011:rxXV4pGzxLJgxaXQ@cluster0.undjh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002442237854'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "-1002046895970") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
