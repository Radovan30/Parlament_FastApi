from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import get_db, Categories, DrinkTypes, Drinks
from app.services.daily_menu_service import add_daily_menu, delete_daily_menu
from pydantic import BaseModel
from datetime import date
from app.utils.auth import verify_admin
from app.schemas_drink import CategoryCreate, DrinkTypeCreate, DrinkCreate, DrinkTypeResponse, CategoryResponse, DrinkUpdate, DrinkResponse

router = APIRouter()


class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def admin_login(request: LoginRequest, db: Session = Depends(get_db)):
    token = verify_admin(request.username, request.password, db)

    if not token:
        raise HTTPException(status_code=401, detail="Špatné jméno nebo heslo!")

    return token


class DailyMenuCreate(BaseModel):
    date: date
    soup: str
    meal_1: str
    meal_1_price: float
    meal_2: str
    meal_2_price: float
    meal_3: str
    meal_3_price: float

@router.post("/daily-menu")
def create_daily_menu(menu: DailyMenuCreate, db: Session = Depends(get_db)):
    return add_daily_menu(**menu.model_dump(), db=db)

@router.delete("/daily-menu/{menu_id}")
def remove_daily_menu(menu_id: int, db: Session = Depends(get_db)):
    if delete_daily_menu(menu_id, db):
        return {"message": "Menu deleted"}
    raise HTTPException(status_code=404, detail="Menu not found")



#
#   NÁPOJE
#

# CREATE
#
# 1. Vytvoření nové kategorie
@router.post("/categories/create", response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    new_category = Categories(name=category.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

# 2. Přidání nového nápoje
@router.post("/drinks", response_model=DrinkCreate)
def create_drink(drink: DrinkCreate, db: Session = Depends(get_db)):
    new_drink = Drinks(
        drink_name=drink.drink_name,
        category_id=drink.category_id,
        drink_type_id=drink.drink_type_id,
        volume=drink.volume,
        price=drink.price,
        description=drink.description
    )
    db.add(new_drink)
    db.commit()
    db.refresh(new_drink)
    return new_drink


# 3. Vytvoření nového typu nápoje
@router.post("/drink-types/create", response_model=DrinkTypeCreate)
def create_drink_type(drink_type: DrinkTypeCreate, db: Session = Depends(get_db)):
    new_drink_type = DrinkTypes(name=drink_type.name)
    db.add(new_drink_type)
    db.commit()
    db.refresh(new_drink_type)
    return new_drink_type



# GET
#
# 1. Získání všech kategorií
@router.get("/categories/all", response_model=list[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return db.query(Categories).all()

# 2. Získání nápojů podle kategorie
@router.get("/drinks/by-category/{category_id}", response_model=list[DrinkResponse])
def get_drinks_by_category(category_id: int, db: Session = Depends(get_db)):
    drinks = db.query(Drinks).filter(Drinks.category_id == category_id).all()
    return drinks

# 3. Získání všech typů nápojů
@router.get("/drink-types", response_model=list[DrinkTypeResponse])
def get_drink_types(db: Session = Depends(get_db)):
    return db.query(DrinkTypes).all()



# PUT
#
# 1. Aktualizace kategorie nápojů
@router.put("/categories/{category_id}", response_model=CategoryResponse)
def update_category(category_id: int, category_data: CategoryCreate, db: Session = Depends(get_db)):
    category = db.query(Categories).filter(Categories.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Kategorie nenalezena")

    category.name = category_data.name
    db.commit()
    db.refresh(category)
    return category

# 2. Aktualizace nápoje
@router.put("/drinks/{drink_id}", response_model=DrinkCreate)
def update_drink(drink_id: int, drink_data: DrinkUpdate, db: Session = Depends(get_db)):
    drink = db.query(Drinks).filter(Drinks.id == drink_id).first()
    if not drink:
        raise HTTPException(status_code=404, detail="Nápoj nenalezen")

    drink.drink_name = drink_data.drink_name
    drink.category_id = drink_data.category_id
    drink.drink_type_id = drink_data.drink_type_id
    drink.volume = drink_data.volume
    drink.price = drink_data.price
    drink.description = drink_data.description

    db.commit()
    db.refresh(drink)
    return drink

# 3. Aktualizace typu nápoje
@router.put("/drink-types/{drink_type_id}", response_model=DrinkTypeCreate)
def update_drink_type(drink_type_id: int, drink_type_data: DrinkTypeCreate, db: Session = Depends(get_db)):
    drink_type = db.query(DrinkTypes).filter(DrinkTypes.id == drink_type_id).first()
    if not drink_type:
        raise HTTPException(status_code=404, detail="Typ nápoje nenalezen")

    drink_type.name = drink_type_data.name
    db.commit()
    db.refresh(drink_type)
    return drink_type



# DELET
#
# 1. Smazání kategorie
@router.delete("/categories/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(Categories).filter(Categories.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Kategorie nenalezena")
    db.delete(category)
    db.commit()
    return {"message": "Kategorie smazána"}

# 2. Smazání nápoje
@router.delete("/drinks/{drink_id}")
def delete_drink(drink_id: int, db: Session = Depends(get_db)):
    drink = db.query(Drinks).filter(Drinks.id == drink_id).first()
    if not drink:
        raise HTTPException(status_code=404, detail="Nápoj nenalezen")
    db.delete(drink)
    db.commit()
    return {"message": "Nápoj smazán"}

# 3. Smazání typu nápoje
@router.delete("/drink-types/{drink_type_id}")
def delete_drink_type(drink_type_id: int, db: Session = Depends(get_db)):
    drink_type = db.query(DrinkTypes).filter(DrinkTypes.id == drink_type_id).first()
    if not drink_type:
        raise HTTPException(status_code=404, detail="Typ nápoje nenalezen")
    db.delete(drink_type)
    db.commit()
    return {"message": "Typ nápoje smazán"}
