import pytest
from sqlalchemy.orm import sessionmaker
from app.auth import verify_admin
from app.models import Base, engine, AdminUser
from werkzeug.security import generate_password_hash

# Vytvoříme session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    db = SessionLocal()
    admin = AdminUser(username="testadmin", password_hash=generate_password_hash("testpass"))
    db.add(admin)
    db.commit()
    db.close()
    yield  # Po testech se databáze může smazat

@pytest.fixture
def db():
    """Fixture pro testovací databázovou session"""
    session = SessionLocal()
    yield session
    session.close()

def test_verify_admin(db):
    assert verify_admin("testadmin", "testpass", db) is True
    assert verify_admin("root", "sacret", db) is False
    assert verify_admin("nonexistent", "testpass", db) is False

