import re, os

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
API_ID = int(environ.get('API_ID', '10651048'))
API_HASH = environ.get('API_HASH', '37775aca7d11f450ecde375baac17fe7')
BOT_TOKEN = environ.get('BOT_TOKEN', '5473562541:AAGiYVUx1fNiXLs_KiTKoH9pJ0fAhYXUhK0')

FORCE_SUB = os.environ.get("FORCE_SUB", "Aguniversmovie") 

DB_NAME = os.environ.get("DB_NAME","gowtham")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Aadhi:42426840@cluster0.h9rky.mongodb.net/?retryWrites=true&w=majority")
 
DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://apex:aadhi@8.219.177.252:5432/apexdb") 

FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/e7aba0e06227ffd054728.jpg")

ADMIN = os.environ.get("ADMIN", "1323557247") 
