from sqlalchemy.orm import Session
from app.models import AdminUser
from werkzeug.security import generate_password_hash, check_password_hash

# Vytvoření nového admina (použití jednou)
def create_admin_user(username: str, password: str, db: Session):
    password_hash = generate_password_hash(password)
    admin = AdminUser(username=username, password_hash=password_hash)
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin

# Ověření přihlášení admina
def verify_admin(username: str, password: str, db: Session) -> bool:
    user = db.query(AdminUser).filter(AdminUser.username == username).first()
    if user and check_password_hash(user.password_hash, password):
        return True
    return False
