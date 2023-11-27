from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.api.depend import oauth2
from app.api.depend.user import get_current_user_active
from app.api.response.response import make_response_json
from app.api.response.response import make_response_json_4_param
from app.db.database import get_db
from app.model.user import User
from app.schemas.comment import CommentCreate
from app.schemas.comment import CommentUpdate
from app.services.comment import CommentService

router = APIRouter()


@router.get("/comment/{pk}")
def get_comment_by_post(pk: str, skip: int = 0, limit: int = 10,
                        db: Session = Depends(get_db),
                        user: User = Depends(oauth2.get_current_user)):
    service = CommentService(db=db)
    response, count = service.get_comment_by_post(id_sport=pk, skip=skip, limit=limit)
    return make_response_json_4_param(data=response, count=count, status=200, message="get success")


@router.post("/comment/create")
def create_comment(comment_in: CommentCreate, db: Session = Depends(get_db),
                   user: User = Depends(oauth2.get_current_user)):
    service = CommentService(db=db)
    response = service.create_comnent_to_post(user_id=user.id, comment_in=comment_in)
    return make_response_json(data=response, status=200, message="create comment success")


@router.put("/comment/update")
def update_comment(comment_update: CommentUpdate, db: Session = Depends(get_db),
                   user: User = Depends(oauth2.get_current_user)):
    service = CommentService(db=db)
    response = service.update_comment_of_user(user_id=user.id, comment_in=comment_update)
    return make_response_json(data=response, status=200, message="update comment success")


@router.delete("/comment/{pk}")
def remove_commnet(pk: str, user: User = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    service = CommentService(db=db)
    response = service.remove_comment_by_id(user=user, comment_id=pk)
    return make_response_json(data=response, status=200, message="deleted success")
