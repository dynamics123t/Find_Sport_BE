from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.schemas.user import UserInfo

class SportBase(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    img: Optional[str] = None
    address: Optional[str] = None
    price: Optional[str] = None

    class Config:
        orm_mode = True

class SportCreateParams(BaseModel):
    name: str
    img: str
    address: str
    price: str
class SportCreate(SportBase):
    pass

class SportUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    img: Optional[str] = None
    address: Optional[str] = None
    price: Optional[str] = None

class SportResponse(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    img: Optional[str] = None
    description: Optional[str] = None
    price: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    time_create: Optional[datetime] = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
