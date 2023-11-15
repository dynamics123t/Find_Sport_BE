from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.model.base import TypeSport
from app.schemas.user import UserInfo


class SportBase(BaseModel):
    name: Optional[str] = None
    img: Optional[str] = None
    address: Optional[str] = None
    price: Optional[str] = None
    description: Optional[str] = None
    phone: Optional[str] = None
    sports_field: Optional[TypeSport] = TypeSport.SOCCER


    class Config:
        orm_mode = True


class SportCreateParams(BaseModel):
    name: str
    img: str
    address: str
    price: str


class SportCreate(SportBase):
    id: Optional[str] = None
    created_by: Optional[str] = None


class SportUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    img: Optional[str] = None
    address: Optional[str] = None
    price: Optional[str] = None
    sports_field: Optional[TypeSport] = TypeSport.SOCCER

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
