import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.crud.recomment import recomment
from app.model.user import User
from app.schemas.recomment import RecommentCreate
from app.schemas.recomment import RecommentResponse
from app.schemas.recomment import RecommentUpdate


class RecommentService:
    def __init__(self, db: Session):
        self.db = db

    def create_recomnent_to_post(self, user_id: str, recomment_in: RecommentCreate):
        recomment_in.id = uuid.uuid4()
        recomment_in.id_user = user_id
        result = recomment.create(db=self.db, obj_in=recomment_in)
        self.db.commit()
        return RecommentResponse.from_orm(result)

    def update_recomment_of_user(self, user_id: str, recomment_in: RecommentUpdate):
        comment_db = recomment.get(db=self.db, entry_id=recomment_in.id)
        if comment_db is None:
            raise HTTPException(status_code=400, detail="RECOMMENT NOT AVAILABLE")
        if comment_db.id_user != user_id:
            raise HTTPException(status_code=401, detail="ban ko phai nguoi so huu")
        return recomment.update(db=self.db, db_obj=comment_db, obj_in=recomment_in)

    def get_count_recomment_by_comment(self, id_recomment: str):
        return recomment.get_count_recomment_by_commet(db=self.db, id_comment=id_recomment)

    def get_recomment_by_comment(self, id_comment: str, skip: int, limit: int):
        data, count = recomment.get_recomment_by_comment(db=self.db, id_comment=id_comment, skip=skip, limit=limit)
        response = []
        for item in data:
            response.append(RecommentResponse.from_orm(item))
        return response, count

    # def get_comment_by_post(self, id_sport: str, skip: int, limit: int):
    #     data, count = comment.get_comment_by_post(db=self.db, id_sport=id_sport, skip=skip, limit=limit)
    #     response = []
    #     for item in data:
    #         response.append(CommentResponse.from_orm(item))
    #     return response, count

    def remove_recomment_by_id(self, user: User, recomment_id: str):
        data = recomment.get(db=self.db, entry_id=recomment_id)
        if data.id_user != user.id:
            raise HTTPException(status_code=401, detail="ko phai nguoi so huu")
        status = recomment.remove(db=self.db, entry_id=recomment_id)
        self.db.commit()
        return status