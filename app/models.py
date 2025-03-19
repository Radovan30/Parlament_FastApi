from sqlalchemy import Column, Integer, String, Boolean, DECIMAL, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from db.database import Base, SessionLocal



# Admin
class AdminUser(Base):
    __tablename__ = "admin_users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)



# Model pro denní menu
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



# Kategorie nápojů
class Categories(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)

    # Vazba na nápoje
    drinks = relationship("Drinks", back_populates="category")

# Typy nápojů
class DrinkTypes(Base):
    __tablename__ = "drink_types"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)

    # Vazba na nápoje
    drinks = relationship("Drinks", back_populates="drink_type")

# Model pro nápoje
class Drinks(Base):
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



# Kategorie jídel
class FoodCategory(Base):
    __tablename__ = 'food_categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    # Vztah k jídlům
    foods = relationship("Foods", back_populates="category")

# Hlavní tabulka jídel
class Foods(Base):
    __tablename__ = 'foods'

    id = Column(Integer, primary_key=True, index=True)
    food_name = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('food_categories.id'), nullable=False)
    weight = Column(DECIMAL(5, 2), nullable=False)
    price = Column(DECIMAL(6, 2), nullable=False)
    description = Column(Text, nullable=True)
    is_special = Column(Boolean, default=False, nullable=False)
    image_url = Column(String, nullable=True)

    # Vztah ke kategorii jídel
    category = relationship("FoodCategory", back_populates="foods")

    # Vztah k alergenům (M:N vztah přes FoodAllergen)
    allergens = relationship("Allergen", secondary="food_allergens", back_populates="foods")



# Tabulka alergenů
class Allergen(Base):
    __tablename__ = 'allergens'

    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer, unique=True, nullable=False)
    name = Column(String, nullable=False)

    # Vztah k jídlům přes spojovací tabulku
    foods = relationship("Foods", secondary="food_allergens", back_populates="allergens")


# Spojovací tabulka pro jídla a alergeny (M:N vztah)
class FoodAllergen(Base):
    __tablename__ = 'food_allergens'

    food_id = Column(Integer, ForeignKey('foods.id'), primary_key=True)
    allergen_id = Column(Integer, ForeignKey('allergens.id'), primary_key=True)


# Tabulka panel
class Panel(Base):
    __tablename__ = "panels"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    description1 = Column(String, nullable=True)
    description2 = Column(String, nullable=True)
    date_start = Column(Date, nullable=True)
    date_end = Column(Date, nullable=True)
    visible = Column(Boolean, default=True)



def get_db():
    """ Dependency FastAPI pro získání DB session """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

