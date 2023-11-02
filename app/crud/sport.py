from typing import Union, Dict, Any

from sqlalchemy.orm import Session

from app.constant.app_status import AppStatus
from app.core.exceptions import error_exception_handler
from app.crud.base import CRUDBase, ModelType, UpdateSchemaType
from app.model.sport import Sport
from app.schemas.sport import SportCreate
from app.schemas.sport import SportUpdate

class CRUDSport(CRUDBase[Sport, SportCreate, SportUpdate]):

    def create(self, db: Session, data_create: SportCreate):
        result = super().create(db=db, obj_in=data_create)
        return result

    def update( self,db: Session,sport_id: str, data_update: Union[UpdateSchemaType, Dict[str, Any]]) -> Sport:
        current_sport = self.get(db=db, entry_id=sport_id)
        if not current_sport:
            raise error_exception_handler(error=Exception, app_status=AppStatus.ERROR_404_NOT_FOUND)
        result = super().update(db=db, db_obj=current_sport, obj_in=data_update)
        return result
    def remove(self, db: Session, *, sport_id: str) -> ModelType:
        current_sport = self.get(db=db, entry_id=sport_id)
        if not current_sport:
            raise error_exception_handler(error=Exception, app_status=AppStatus.ERROR_404_NOT_FOUND)
        result = super().remove(db=db, entry_id=sport_id)
        return result

sport = CRUDSport(Sport)