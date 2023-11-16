import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.constant.app_status import AppStatus
from app.core.exceptions import error_exception_handler
from app.crud.comment import comment

from app.crud.sport import sport
from app.model.user import User
from app.schemas import SportBase
from app.schemas.sport import SportCreate
from app.schemas.sport import SportResponse
from app.schemas.sport import SportUpdate


class PostService:
    def __init__(self, db: Session):
        self.db = db

    def create_sport(self, sport_cr: SportBase, user_id: str):
        db_create = SportCreate(id=uuid.uuid4().__str__(), **sport_cr.dict(), created_by=user_id)
        result = sport.create(db=self.db, data_create=db_create)
        self.db.commit()
        return SportResponse.from_orm(result)

    def update_sport(self, sport_update: SportUpdate, sport_id: str):
        post_in = sport.get(db=self.db, entry_id=sport_id)
        if post_in is None:
            raise HTTPException(status_code=400, detail="SPORT NOT AVAILABLE")
        result = sport.update(db=self.db, sport_id=sport_id, data_update=sport_update)
        self.db.commit()
        return result

    def remove_sport(self, sport_id: str):
        current_sport = sport.get(db=self.db, entry_id=sport_id)
        if not current_sport:
            raise error_exception_handler(error=Exception, app_status=AppStatus.ERROR_404_NOT_FOUND)
        result = sport.remove(db=self.db, sport_id=sport_id)
        return result

    def get_sport(self, sport_id: str):
        p = sport.get(self.db, sport_id)
        response = SportResponse.from_orm(p)
        response.comment_count = comment.get_count_comment_by_spost(self.db, p.id)
        return response

    def get_sport_of_me(self, name: str, skip: int, limit: int):
        result, count = sport.get_sport_by_me(db=self.db, name=name, skip=skip, limit=limit)
        response = []
        return response, count

    def get_sport_by_id(self, sport_id: str):
        result = sport.get(db=self.db, entry_id=sport_id)
        return result

    def get_all(self, name: str, skip: int, limit: int):
        return sport.get_sport(db=self.db, name=name, skip=skip, limit=limit)
