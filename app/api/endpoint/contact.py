from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session


from app.db.database import get_db

from ..depend import oauth2
from ...model import User

from ...schemas.contact import ContactBase

from ...services.contact import ContactService

router = APIRouter()


@router.post("/contact/create")
async def create_contact(request: ContactBase, db: Session = Depends(get_db),
                         user: User = Depends(oauth2.get_current_active_user)):
    service = ContactService(db=db)
    result = await service.create_contact(data_create=request, user_id=user.id)
    return result


@router.get("/contact/get")
async def get_contact(skip: int = 0, limit: int = 10, user: User = Depends(oauth2.admin),
                      db: Session = Depends(get_db)):
    service = ContactService(db=db)
    result = await service.get_multi_contact(skip, limit)
    return result
