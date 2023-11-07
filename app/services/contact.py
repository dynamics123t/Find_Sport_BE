import uuid

from sqlalchemy.orm import Session

from app.crud.contact import crud_contact
from app.model.user import User
from app.schemas.contact import ContactCreate, ContactBase


class ContactService:
    def __init__(self, db: Session):
        self.db = db

    async def create_contact(self, data_create: ContactBase, user_id: str):
        db_create = ContactCreate(id=uuid.uuid4().__str__(), user_id=user_id, content = data_create.content)
        result = crud_contact.create(db=self.db, obj_in=db_create)
        return result

    async def get_multi_contact(self, skip:int, limit:int):
        result = crud_contact.get_contact(db=self.db, skip=skip, limit=limit)
        return result