from sqlalchemy import Column, Integer, String, DECIMAL, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import create_engine
from config import DATABASE_URL

Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine, autoflush=False)

# ✅ Admin
class AdminUser(Base):
    __tablename__ = "admin_users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

# ✅ Model pro denní menu
class DailyMenu(Base):
    __tablename__ = "daily_menu"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)  # ✅ Správně importováno z SQLAlchemy
    soup = Column(String(255), nullable=False)
    meal_1 = Column(String(255), nullable=False)
    meal_1_price = Column(DECIMAL(5,2), nullable=False)
    meal_2 = Column(String(255), nullable=False)
    meal_2_price = Column(DECIMAL(5,2), nullable=False)
    meal_3 = Column(String(255), nullable=False)
    meal_3_price = Column(DECIMAL(5,2), nullable=False)

# ✅ Kategorie nápojů
class Categories(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)

    # Vazba na nápoje
    drinks = relationship("Drinks", back_populates="category")

# ✅ Typy nápojů
class DrinkTypes(Base):
    __tablename__ = "drink_types"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)

    # Vazba na nápoje
    drinks = relationship("Drinks", back_populates="drink_type")

# ✅ Model pro nápoje
class Drinks(Base):  # ✅ Ujistěte se, že je to "Drinks", ne "Drink"
    __tablename__ = "drinks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    drink_name = Column(String(255), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    drink_type_id = Column(Integer, ForeignKey("drink_types.id"), nullable=False)
    volume = Column(DECIMAL(4,2), nullable=False)
    price = Column(DECIMAL(5,2), nullable=False)
    description = Column(String(500), nullable=True)

    # Vazby na kategorie a typy nápojů
    category = relationship("Categories", back_populates="drinks")
    drink_type = relationship("DrinkTypes", back_populates="drinks")

def get_db():
    """ Dependency FastAPI pro získání DB session """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

