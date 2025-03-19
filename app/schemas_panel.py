from typing import Optional
from pydantic import BaseModel
import datetime

class PanelBase(BaseModel):
    title: str
    description1: Optional[str] = None
    description2: Optional[str] = None  #
    date_start: Optional[datetime.date] = None
    date_end: Optional[datetime.date] = None
    visible: bool

class PanelCreate(PanelBase):
    pass

class PanelUpdate(BaseModel):
    title: Optional[str] = None
    description1: Optional[str] = None
    description2: Optional[str] = None
    date_start: Optional[datetime.date] = None
    date_end: Optional[datetime.date] = None
    visible: Optional[bool] = None

class PanelResponse(PanelBase):
    id: int

    class Config:
        orm_mode = True