class Config(object):
    LOGGER = True

    API_KEY = "7010583697:AAFF5koxJP2bP7vCxNASJeg72MQKlyhqmFY"
    OWNER_ID = "6805772957"
    OWNER_USERNAME = "kingtrex777"
    
    MONGO_DB_URL = 'mongodb+srv://luffytarooor:VjcfPWuhh2yGCFGm@cluster0.qxknmsd.mongodb.net/'
    MESSAGE_DUMP = None
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = None

    SUDO_USERS = []
    SUPPORT_USERS = []
    WHITELIST_USERS = []
    DONATION_LINK = None
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False
    STRICT_GBAN = False
    WORKERS = 8
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'
    ALLOW_EXCL = False


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
  
