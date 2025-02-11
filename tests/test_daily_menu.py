import pytest
from sqlalchemy.orm import Session
from app.models import Base, engine, DailyMenu


@pytest.fixture
def db():
    """Fixture pro testovací databázovou session"""
    session = Session(bind=engine)
    yield session
    session.close()

def test_daily_menu_insertion(db):
    item = DailyMenu(
        date="2025-01-01",
        soup="Hovězí vývar",
        meal_1="Svíčková na smetaně",
        meal_1_price=150.00,
        meal_2="Kuřecí steak s rýží",
        meal_2_price=130.00,
        meal_3="Vegetariánské rizoto",
        meal_3_price=120.00
    )
    db.add(item)
    db.flush()
    print(f"Meal 1 price before commit: {item.meal_1_price}")
    db.commit()

    result = db.query(DailyMenu).filter_by(meal_1="Svíčková na smetaně").first()
    assert result is not None
    assert result.meal_1_price == 150.00



