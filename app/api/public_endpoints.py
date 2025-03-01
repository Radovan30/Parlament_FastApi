from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import get_db
from app.services.daily_menu_service import get_daily_menu_by_date, get_all_menus
from app.services.drinks_service import Drinks, Categories, DrinkTypes
from app.services.foods_service import Foods, FoodCategory, Allergen
from datetime import date

router = APIRouter()

@router.get("/daily-menu/today")
def get_today_menu(db: Session = Depends(get_db)):
    menu = get_daily_menu_by_date(date.today(), db)
    if menu:
        return menu
    return {"message": "No menu available for today"}


@router.get("/daily-menu/all")
def get_all_daily_menus(db: Session = Depends(get_db)):
    print("Endpoint `/daily-menu/all` byl zavolán!")
    menus = get_all_menus(db)
    if not menus:
        return {"message": "No menus found"}
    return menus


# Pomocná funkce pro formátování odpovědi o nápoji
def format_drink_response(drink):
    return {
        "id": drink.id,
        "drink_name": drink.drink_name,
        "category": drink.category.name if drink.category else None,
        "drink_type": drink.drink_type.name if drink.drink_type else None,
        "volume": drink.volume,
        "price": drink.price,
        "description": drink.description
    }

# Endpoint pro získání všech nápojů
@router.get("/drinks/all")
def get_public_drinks(db: Session = Depends(get_db)):
    drinks = db.query(Drinks).join(Categories).join(DrinkTypes).all()
    if not drinks:
        raise HTTPException(status_code=404, detail="No drinks found")
    return [format_drink_response(drink) for drink in drinks]



# Endpoint pro získání konkrétního nápoje podle ID
@router.get("/drinks/{drink_id}")
def get_public_drink_by_id(drink_id: int, db: Session = Depends(get_db)):
    drink = db.query(Drinks).join(Categories).join(DrinkTypes).filter(Drinks.id == drink_id).first()
    if not drink:
        raise HTTPException(status_code=404, detail="Drink not found")
    return format_drink_response(drink)


# Endpoint pro získání všech kategorií
@router.get("/categories/all")
def get_all_categories(db: Session = Depends(get_db)):
    categories = db.query(Categories).all()

    if not categories:
        raise HTTPException(status_code=404, detail="No categories found")

    return [{"id": category.id, "name": category.name} for category in categories]


# Endpoint pro získání nápojů podle kategorie
@router.get("/drinks/by-category/{category_id}")
def get_drinks_by_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(Categories).filter(Categories.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    drinks = db.query(Drinks).filter(Drinks.category_id == category_id).join(Categories).join(DrinkTypes).all()
    return [format_drink_response(drink) for drink in drinks]



# Pomocná funkce pro formátování odpovědi o jídlech
def format_food_response(food):
    return {
        "id": food.id,
        "food_name": food.food_name,
        "category": food.category.name if food.category else None,
        "weight": float(food.weight),
        "price": float(food.price),
        "description": food.description,
        "is_special": food.is_special,
        "image_url": food.image_url,
        "allergens": [{"code": allergen.code, "name": allergen.name} for allergen in food.allergens]
    }

# Endpoint pro získání všech jídel
@router.get("/foods/all")
def get_public_foods(db: Session = Depends(get_db)):
    foods = db.query(Foods).all()
    return [format_food_response(food) for food in foods]

# Endpoint pro získání konkrétního jídla podle ID
@router.get("/foods/{food_id}")
def get_public_food_by_id(food_id: int, db: Session = Depends(get_db)):
    food = db.query(Foods).filter(Foods.id == food_id).first()
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")
    return format_food_response(food)

# Endpoint pro získání všech kategorií jídel
@router.get("/food-categories/all")
def get_all_food_categories(db: Session = Depends(get_db)):
    categories = db.query(FoodCategory).all()
    if not categories:
        raise HTTPException(status_code=404, detail="No categories found")
    return [{"id": category.id, "name": category.name} for category in categories]

# Endpoint pro získání jídel podle kategorie
@router.get("/foods/by-category/{category_id}")
def get_foods_by_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(FoodCategory).filter(FoodCategory.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    foods = db.query(Foods).filter(Foods.category_id == category_id).all()
    return [format_food_response(food) for food in foods]

# Endpoint pro získání všechny alergeny
@router.get("/food-allergens/all")
def get_all_food_allergens(db: Session = Depends(get_db)):
    allergens = db.query(Allergen).all()
    if not allergens:
        raise HTTPException(status_code=404, detail="No categories found")
    return [{"id": allergen.id,"code": allergen.code ,"name": allergen.name} for allergen in allergens]
