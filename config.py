import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "10651048")

API_HASH = os.environ.get("API_HASH", "37775aca7d11f450ecde375baac17fe7")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "2103300889:AAEVZd_cAFHdJDU-hAYOdYtwALFwACETP2A") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Aguniversmovie") 

DB_NAME = os.environ.get("DB_NAME","gowtham")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Aadhi:42426840@cluster0.h9rky.mongodb.net/?retryWrites=true&w=majority")
 
DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://apex:aadhi@8.219.177.252:5432/apexdb") 

FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/e7aba0e06227ffd054728.jpg")

ADMIN = os.environ.get("ADMIN", "1323557247") 
