import uuid
from datetime import date

from sqlalchemy.orm import Session

from app.crud.booking import booking
from app.model.base import StatusBookingEnum
from app.schemas.booking import BookingBase, BookingCreate, BookingUpdate


class BookingService:
    def __init__(self, db: Session):
        self.db = db

    async def create_booking(self, request: BookingBase, user_id: str):
        if len(request.time) == 1:
            data_create = BookingCreate(**request.dict(), id=uuid.uuid4().__str__(), id_user=user_id)
            response = booking.create(db=self.db, obj_in=data_create)
        else:
            date_create = [BookingCreate(**request.custom_dict(), id=uuid.uuid4().__str__(), id_user=user_id, time=time)
                           for time in request.time]

            booking.bulk_save_objects(db=self.db, obj_ins=date_create)
            response = "BOOKING SUCCESS"
        return response

    async def update_status(self, booking_id: str, status: StatusBookingEnum):
        current_booking = booking.get(db=self.db, entry_id=booking_id)
        data_update = dict(status=status)
        return booking.update(db=self.db, db_obj=current_booking, obj_in=data_update)

    async def update_scheduler_booking(self, booking_id: str, request: BookingUpdate):
        current_booking = booking.get(db=self.db, entry_id=booking_id)
        return booking.update(db=self.db, db_obj=current_booking, obj_in=request)

    async def get_booking(self, booking_id: str, skip: int, limit: int):
        if booking_id:
            return booking.get(db=self.db, entry_id=booking_id), 1
        else:
            result, count = booking.get_list_bookings(skip, limit)
            return result, count

    async def get_bookings_sport(self, sport_id: str, date_booking: date, skip: int, limit: int):
        result = booking.get_list_booking_by_sport_id(db=self.db, sport_id=sport_id, date_booking=date_booking,
                                                      skip=skip, limit=limit)
        return result
