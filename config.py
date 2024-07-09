import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "25797857")

API_HASH = os.environ.get("API_HASH", "77717127ece56fac64ebea6250db8bb7")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7457461506:AAHlxmzou4DwiXzYKKd2NDcAwHnPbSCBjPg") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1002005092018") 

DB_NAME = os.environ.get("DB_NAME","renamer")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Venkat3823:Venkat3823@cluster0.ig0oc9y.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6693549185').split()]

PORT = os.environ.get("PORT", "8080")
