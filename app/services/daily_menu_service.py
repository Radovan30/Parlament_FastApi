from sqlalchemy.orm import Session
from app.models import DailyMenu

# Přidání nového denního menu
def add_daily_menu(date, soup, meal_1, meal_1_price, meal_2, meal_2_price, meal_3, meal_3_price, db: Session):
    menu = DailyMenu(
        date=date,
        soup=soup,
        meal_1=meal_1,
        meal_1_price=meal_1_price,
        meal_2=meal_2,
        meal_2_price=meal_2_price,
        meal_3=meal_3,
        meal_3_price=meal_3_price
    )
    db.add(menu)
    db.commit()
    db.refresh(menu)
    return menu


# ✅ Získání denního menu podle data
def get_daily_menu_by_date(date, db: Session):
    return db.query(DailyMenu).filter(DailyMenu.date == date).first()

# ✅ Smazání denního menu
def delete_daily_menu(menu_id, db: Session):
    menu = db.query(DailyMenu).filter(DailyMenu.id == menu_id).first()
    if menu:
        db.delete(menu)
        db.commit()
        return True
    return False

# ✅ Získání celého denního menu
def get_all_menus(db: Session):
    return db.query(DailyMenu).all()
