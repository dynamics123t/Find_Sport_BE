from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ContactBase(BaseModel):
    content: Optional[str] = None


class ContactCreate(ContactBase):
    id: Optional[str] = None
    user_id: Optional[str] = None
    created_at: Optional[datetime] = None

class ContactUpdate(ContactBase):
    pass


class ContactResponse(BaseModel):
    id: Optional[str] = None
    user_id: Optional[str] = None
    created_at: Optional[datetime] = None
    class Config:
        orm_mode = True
