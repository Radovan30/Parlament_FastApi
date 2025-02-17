import os
import secrets

from dotenv import load_dotenv

load_dotenv()  # Načte proměnné z .env

# Získání proměnných z .env, bez výchozích hodnot
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_DB = os.getenv("MYSQL_DB")
SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    SECRET_KEY = secrets.token_hex(32)  # Vygeneruje nový bezpečný klíč
    with open(".env", "a") as env_file:  # Přidá ho do `.env` souboru
        env_file.write(f"\nSECRET_KEY={SECRET_KEY}\n")
    print("✅ Vygenerován nový SECRET_KEY a uložen do .env")

# Ověření, že všechny proměnné jsou nastavené
if not all([MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DB, SECRET_KEY]):
    raise ValueError("❌ Chyba: Některé environment proměnné (MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DB, SECRET_KEY) nejsou nastavené v .env souboru!")

# Sestavení URL pro připojení k databázi
DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"


