from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.api.depend.user import get_current_user_active
from app.api.response.response import make_response_json
from app.api.response.response import make_response_json_4_param
from app.db.database import get_db
from app.model.user import User
from app.schemas.recomment import RecommentCreate
from app.schemas.recomment import RecommentUpdate
from app.services.recomment import RecommentService

router = APIRouter()


@router.get("/recomment/{pk}")
def get_recomment_by_post(pk: str, skip: int = 0, limit: int = 10,
                          db: Session = Depends(get_db),
                          user: User = Depends(get_current_user_active)):
    service = RecommentService(db=db)
    response, count = service.get_recomment_by_comment(id_comment=pk, skip=skip, limit=limit)
    return make_response_json_4_param(data=response, count=count, status=200, message="get success")


@router.post("/recomment/create")
def create_recomment(recomment_in: RecommentCreate, db: Session = Depends(get_db),
                     user: User = Depends(get_current_user_active)):
    service = RecommentService(db=db)
    response = service.create_recomnent_to_post(user_id=user.id, recomment_in=recomment_in)
    return make_response_json(data=response, status=200, message="reate comment success")


@router.put("/recomment/update")
def update_recomment(comment_update: RecommentUpdate, db: Session = Depends(get_db),
                     user: User = Depends(get_current_user_active)):
    service = RecommentService(db=db)
    response = service.update_recomment_of_user(user_id=user.id, recomment_in=comment_update)
    return make_response_json(data=response, status=200, message="update comment success")


@router.delete("/recomment/{pk}")
def remove_recomment(pk: str, user: User = Depends(get_current_user_active), db: Session = Depends(get_db)):
    service = RecommentService(db=db)
    response = service.remove_recomment_by_id(user, pk)
    return make_response_json(data=response, status=200, message="deleted success")
