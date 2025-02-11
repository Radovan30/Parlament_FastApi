import os
from dotenv import load_dotenv

load_dotenv()  # Načte proměnné z .env

# Získání proměnných z .env, bez výchozích hodnot
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_DB = os.getenv("MYSQL_DB")
SECRET_KEY = os.getenv("SECRET_KEY")

# Ověření, že všechny proměnné jsou nastavené
if not all([MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DB, SECRET_KEY]):
    raise ValueError("❌ Chyba: Některé environment proměnné (MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DB, SECRET_KEY) nejsou nastavené v .env souboru!")

# Sestavení URL pro připojení k databázi
DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"


