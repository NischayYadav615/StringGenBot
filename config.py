from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("19911978"))
API_HASH = getenv("e3f5848d4c384af9e6f1f52ca84c19c7")

BOT_TOKEN = getenv("6028079887:AAGoPNp6LhbpXkcExuXPVTQeoo24p25rO74")
OWNER_ID = int(getenv("6205468574"))

MONGO_DB_URI = getenv("mongodb+srv://NischayP:NischayP@cluster0.9cuf6ae.mongodb.net/?retryWrites=true&w=majority")
