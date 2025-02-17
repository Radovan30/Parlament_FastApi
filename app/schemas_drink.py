from pydantic import BaseModel
from typing import Optional

class DrinkBase(BaseModel):
    drink_name: str
    category_id: int
    drink_type_id: int
    volume: float
    price: float
    description: Optional[str] = None

    class Config:
        from_attributes = True

class DrinkCreate(DrinkBase):
    pass

class DrinkUpdate(DrinkBase):
    pass

class DrinkResponse(DrinkBase):
    # V odpovědi chceme zobrazit i ID
    id: int

    class Config:
        from_attributes = True

# Model pro vytvoření kategorie nápojů
class CategoryCreate(BaseModel):
    name: str

    class Config:
        from_attributes = True  # Pro kompatibilitu se SQLAlchemy

class CategoryResponse(CategoryCreate):
    id: int

    class Config:
        from_attributes = True

# Model pro vytvoření typu nápojů
class DrinkTypeCreate(BaseModel):
    name: str

    class Config:
        from_attributes = True  # Lepší kompatibilita se SQLAlchemy

class DrinkTypeResponse(DrinkTypeCreate):
    id: int

    class Config:
        from_attributes = True


