from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import get_db
from app.services.daily_menu_service import add_daily_menu, delete_daily_menu
from pydantic import BaseModel
from datetime import date

router = APIRouter()

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


