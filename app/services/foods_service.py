from sqlalchemy.orm import Session
from app.models import Foods, FoodCategory, Allergen, FoodAllergen

# Obecná funkce pro odstranění záznamu podle ID a modelu (Eliminuje duplicitu)
def delete_record_by_id(model, record_id: int, db: Session):
    record = db.get(model, record_id)
    if record:
        db.delete(record)
        db.commit()
        return True
    return False

# Přidání nového jídla
def add_food(food_name: str, category_id: int, weight: float, price: float, description: str, db: Session):
    food = Foods(
        food_name=food_name,
        category_id=category_id,
        weight=weight,
        price=price,
        description=description
    )
    db.add(food)
    db.commit()
    db.refresh(food)
    return food

# Získání všech jídel s detaily o kategorii
def get_all_foods(db: Session):
    return (
        db.query(Foods, FoodCategory.name.label("category_name"))
        .join(FoodCategory, Foods.category_id == FoodCategory.id)
        .all()
    )

# Získání jednoho jídla podle ID
def get_food_by_id(food_id: int, db: Session):
    return (
        db.query(Foods, FoodCategory.name.label("category_name"))
        .join(FoodCategory, Foods.category_id == FoodCategory.id)
        .filter(Foods.id == food_id)
        .first()
    )

# Mazání jídla – Použití obecné funkce
def delete_food(food_id: int, db: Session):
    return delete_record_by_id(Foods, food_id, db)

# Získání všech kategorií jídel
def get_all_food_categories(db: Session):
    return db.query(FoodCategory).all()

# Přidání nové kategorie jídel
def add_food_category(name: str, db: Session):
    category = FoodCategory(name=name)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

# Smazání kategorie jídel – Použití obecné funkce
def delete_food_category(category_id: int, db: Session):
    return delete_record_by_id(FoodCategory, category_id, db)

# Získání všech alergenů
def get_all_allergens(db: Session):
    return db.query(Allergen).all()

# Přidání alergenu
def add_allergen(code: int, name: str, db: Session):
    allergen = Allergen(code=code, name=name)
    db.add(allergen)
    db.commit()
    db.refresh(allergen)
    return allergen

# Přiřazení alergenu k jídlu – Odstranění duplicity
def add_allergen_to_food(food_id: int, allergen_id: int, db: Session):
    if not db.query(Foods).filter(Foods.id == food_id).first():
        print(f"❌ Jídlo s ID {food_id} neexistuje.")
        return None
    if not db.query(Allergen).filter(Allergen.id == allergen_id).first():
        print(f"❌ Alergen s ID {allergen_id} neexistuje.")
        return None

    food_allergen = FoodAllergen(food_id=food_id, allergen_id=allergen_id)
    db.add(food_allergen)
    db.commit()
    return food_allergen

# Získání alergenů pro konkrétní jídlo
def get_allergens_for_food(food_id: int, db: Session):
    return (
        db.query(Allergen)
        .join(FoodAllergen, Allergen.id == FoodAllergen.allergen_id)
        .filter(FoodAllergen.food_id == food_id)
        .all()
    )
