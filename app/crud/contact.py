import uuid

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.model.contact import Contact
from app.schemas.contact import ContactCreate, ContactUpdate, ContactBase


class CRUDContact(CRUDBase[Contact, ContactCreate, ContactUpdate]):

    @staticmethod
    def create_contact(db: Session, db_create: ContactBase, user_id:str):
        db_create = ContactCreate(id=uuid.uuid4().__str__(), **db_create.dict(), user_id=user_id)
        result = super().create(db=db, obj_in=db_create)
        return result

    def get_contact(self, db: Session, skip: int, limit: int):
        result = db.query(self.model).offset(skip).limit(limit).all()
        return result


crud_contact = CRUDContact(Contact)