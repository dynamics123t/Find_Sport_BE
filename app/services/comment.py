import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.crud.comment import comment
from app.model.user import User
from app.schemas.comment import CommentCreate
from app.schemas.comment import CommentResponse
from app.schemas.comment import CommentUpdate


class CommentService:
    def __init__(self, db: Session):
        self.db = db

    def create_comnent_to_post(self, user_id: str, comment_in: CommentCreate):
        comment_in.id = uuid.uuid4()
        comment_in.id_user = user_id
        data = comment.create(db=self.db, obj_in=comment_in, auto_commit=True)
        return CommentResponse.from_orm(data)

    def update_comment_of_user(self, user_id: str, comment_in: CommentUpdate):
        comment_db = comment.get(db=self.db, id=comment_in.id)
        if comment_db is None:
            raise HTTPException(status_code=400, detail="COMMENT NOT AVAILABLE")
        if comment_db.id_user != user_id:
            raise HTTPException(status_code=401, detail="ban ko phai nguoi so huu")
        return comment.update(db=self.db, db_obj=comment_db, obj_in=comment_in)

    def get_count_comment_by_post(self, id_post: str):
        return comment.get_count_comment_by_post(db=self.db, id_post=id_post)

    def get_comment_by_post(self, id_post: str, skip: int, limit: int):
        data, count = comment.get_comment_by_post(db=self.db, id_post=id_post, skip=skip, limit=limit)
        response = []
        for item in data:
            response.append(CommentResponse.from_orm(item))
        return response, count

    def remove_comment_by_id(self, user: User, comment_id: str):
        data = comment.get(db=self.db, id=comment_id)
        if data.id_user != user.id:
            raise HTTPException(status_code=401, detail="ko phai nguoi so huu")
        status = comment.remove(db=self.db, id=comment_id, auto_commit=True)
        self.db.commit()
        return status
