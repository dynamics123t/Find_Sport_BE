import uuid
from datetime import date

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.model.booking import Booking
from app.schemas.booking import BookingCreate, BookingUpdate, BookingBase


class CRUDBooking(CRUDBase[Booking, BookingCreate, BookingUpdate]):
    def get_list_bookings(self, db: Session, skip: int, limit: int):
        db_query = db.query(self.model)
        result = db_query.offset(skip).limit(limit).all()
        # breakpoint()
        return result, db_query.count()

    def get_list_booking_by_sport_id(self, db: Session, sport_id: str, date_booking: date, skip: int, limit: int):
        db_query = db.query(self.model).filter(self.model.id_sport == sport_id, self.model.date_booking == date_booking)
        result = db_query.offset(skip).limit(limit).all()
        return result, db_query.count()

    def create_multi_booking(self, db: Session, request: BookingBase, user_id: str):
        date_create = [
            Booking(**request.custom_dict(), id=uuid.uuid4().__str__(), id_user=user_id, time_booking=time)
            for time in request.time_booking]
        db.bulk_save_objects(date_create)
        db.commit()

    def get_bookings_of_user(self,db: Session, user_id: str, skip:int, limit:int):
        db_query = db.query(self.model).filter(self.model.id_user==user_id)
        count = db_query.count()
        result = db_query.offset(skip).limit(limit).all()
        return result, count



booking = CRUDBooking(Booking)
