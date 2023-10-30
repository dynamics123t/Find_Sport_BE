from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.model.recomment import Recomment
from app.schemas.recomment import RecommentCreate
from app.schemas.recomment import RecommentUpdate


class CRUDRecomment(CRUDBase[Recomment, RecommentCreate, RecommentUpdate]):
    def get_count_recomment_by_comment(self, db: Session, id_comment: str):
        query = db.query(self.model).filter(self.model.id == id_comment).all()
        return query.count()

    def get_recomment_by_comment(self, db: Session, id_comment: str, skip: int, limit: int):
        query = db.query(self.model).filter(self.model.id_cmt == id_comment)
        count = query.count()
        if skip is not None and limit is not None:
            query.offset(skip).limit(limit)
        return query.all(), count


recomment = CRUDRecomment(Recomment)
