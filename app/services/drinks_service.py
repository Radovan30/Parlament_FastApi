from sqlalchemy.orm import Session
from app.models import Drinks, Categories, DrinkTypes

# Přidání nového nápoje
def add_drink(drink_name, category_id, drink_type_id, volume, price, description, db: Session):
    drink = Drinks(
        drink_name=drink_name,
        category_id=category_id,
        drink_type_id=drink_type_id,
        volume=volume,
        price=price,
        description=description
    )
    db.add(drink)
    db.commit()
    db.refresh(drink)
    return drink

# Získání všech nápojů s detaily o kategorii a typu
def get_all_drinks(db: Session):
    return (
        db.query(Drinks, Categories.name.label("category_name"), DrinkTypes.name.label("drink_type_name"))
        .join(Categories, Drinks.category_id == Categories.id)
        .join(DrinkTypes, Drinks.drink_type_id == DrinkTypes.id)
        .all()
    )

# Získání jednoho nápoje podle ID
def get_drink_by_id(drink_id: int, db: Session):
    return (
        db.query(Drinks, Categories.name.label("category_name"), DrinkTypes.name.label("drink_type_name"))
        .join(Categories, Drinks.category_id == Categories.id)
        .join(DrinkTypes, Drinks.drink_type_id == DrinkTypes.id)
        .filter(Drinks.id == drink_id)
        .first()
    )

# Smazání nápoje
def delete_drink(drink_id: int, db: Session):
    drink = db.query(Drinks).filter(Drinks.id == drink_id).first()
    if drink:
        db.delete(drink)
        db.commit()
        return True
    return False

