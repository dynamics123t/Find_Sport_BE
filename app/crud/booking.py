import uuid
from datetime import date

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.model.booking import Booking
from app.schemas.booking import BookingCreate, BookingUpdate


class CRUDBooking(CRUDBase[Booking, BookingCreate, BookingUpdate]):
    def get_list_bookings(self, db: Session, skip: int, limit: int):
        db_query = db.query(self.model)
        result = db_query.offset(skip).limit(limit).all()
        return result, db_query.count()

    def get_list_booking_by_sport_id(self, db: Session, sport_id: str, date_booking: date, skip: int, limit: int):
        db_query = db.query(self.model).filter(self.model.id_sport == sport_id, self.model.date == date_booking)
        result = db_query.offset(skip).limit(limit).all()
        return result, db_query.count()


booking = CRUDBooking(Booking)
