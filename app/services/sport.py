import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.crud.comment import comment

from app.crud.sport import sport
from app.model.user import User
from app.schemas.sport import SportCreate
from app.schemas.sport import SportResponse
from app.schemas.sport import SportUpdate

class Post:
    def __int__(self, db: Session):
        self.db = db

    def create_sport(self, sport_cr: SportCreate):
        sport_cr.id=uuid.uuid4().__str__()
        result = sport.create(db=self.db, obj_in=sport_cr, auto_commit=True)
        self.db.commit()
        return SportResponse.from_orm(result)

    def update_sport(self, sport_cr:SportUpdate):
        post_in = sport.get(db=self.db,id=sport_cr.id)
        if post_in is None:
            raise HTTPException(status_code=400, detail="SPORT NOT AVAILABLE")
        result = sport.update(db=self.db, db_obj=post_in, obj_in=sport_cr)
        self.db.commit()
        return result

    def remove_sport(self, sport_id:str):
        sport.get(db=self.db, id=sport_id)
        result = sport.remove(db=self.db, id=sport_id, auto_commit=True)
        return result

    def get_sport(self, sport_id:str):
        p = sport.get(self.db, sport_id)
        response = SportResponse.from_orm(p)
        response.comment_count = comment.get_count_comment_by_spost(self.db, p.id)
        return response

    def get_all(self):
        return sport.get_multi(db=self.db)