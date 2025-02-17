from sqlalchemy.orm import Session
from app.models import AdminUser
from werkzeug.security import check_password_hash
from dotenv import load_dotenv
from datetime import datetime, timedelta

import jwt
import os

# Načtení proměnných z .env souboru
load_dotenv()

# Tajný klíč pro JWT (nyní načítaný z .env souboru)
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"


# Vytvoření nového admina (použití jednou)
def create_admin_user(username: str, password: str, db: Session):
    user = db.query(AdminUser).filter(AdminUser.username == username).first()

    if not user:
        return None;

    if not check_password_hash(user.password_hash, password):
        return None;

    token_data = {
        "sub": user.username,
        "exp": datetime.utcnow() + timedelta(hours=2),
    }

    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}



# Ověření přihlášení admina a generování JWT tokenu
def verify_admin(username: str, password: str, db: Session):
    user = db.query(AdminUser).filter(AdminUser.username == username).first()
    if user and check_password_hash(user.password_hash, password):
        token_data = {
            "sub": username,
            "exp": datetime.utcnow() + timedelta(hours=2)  # Token platí 2 hodiny
        }
        token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": token}

    return None

