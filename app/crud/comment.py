from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.model.comment import Comment
from app.schemas.comment import CommentCreate
from app.schemas.comment import CommentUpdate


class CRUDComment(CRUDBase[Comment, CommentCreate, CommentUpdate]):

    def get_count_comment_by_post(self, db: Session, id_sport: str):
        query = db.query(self.model).filter(self.model.id_sport == id_sport)
        return query.count()

    def get_comment_by_post(self, db: Session, id_sport: str, skip: int, limit: int):
        query = db.query(self.model).filter(self.model.id_sport == id_sport)
        count = query.count()
        if skip is not None and limit is not None:
            query.offset(skip).limit(limit)
        return query.all(), count


comment = CRUDComment(Comment)