from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.schemas.user import UserInfo


class RecommentBase(BaseModel):
    id: Optional[str] = None
    id_cmt: Optional[str] = None
    content: Optional[str] = None
    image: Optional[str] = None
    time_create: Optional[datetime] = None

    class Config:
        orm_mode = True


class RecommentCreate(RecommentBase):
    id_user: Optional[str] = None


class RecommentUpdate(BaseModel):
    id: Optional[str] = None
    content: Optional[str] = None
    image: Optional[str] = None


class RecommentResponse(BaseModel):
    id: Optional[str] = None
    user: Optional[UserInfo] = None
    id_cmt: Optional[str] = None
    content: Optional[str] = None
    image: Optional[str] = None
    time_create: Optional[datetime] = None

    class Config:
        orm_mode = True
        # allow_population_by_field_name = True
        arbitrary_types_allowed = True
