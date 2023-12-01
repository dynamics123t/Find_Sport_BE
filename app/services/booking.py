import datetime
import uuid
from datetime import date
from sqlalchemy.orm import Session
from fastapi import Request

from app.crud.booking import booking
from app.crud.sport import sport
from app.model.base import StatusBookingEnum, ModeOfPaymentEnum
from app.model.booking import Booking
from app.schemas.booking import BookingBase, BookingCreate, BookingUpdate
from app.utils.payment import payment, payment_return

class BookingService:
    def __init__(self, db: Session):
        self.db = db

    async def create_booking(self, request: Request, booking_cr: BookingBase, user_id: str):
        ids = booking.create_multi_booking(db=self.db, request=booking_cr, user_id=user_id)
        current_sport = sport.get(db=self.db, entry_id=booking_cr.id_sport)
        # total_money = len(booking_cr.time_booking) * current_sport.price * 1
        total_money = current_sport.price
        content = ",".join(ids)
        order_id = int(datetime.datetime.now().timestamp())
        if booking_cr.mode_of_payment == ModeOfPaymentEnum.BANKING:
            response = payment(request=request, amount=total_money, language=str(booking_cr.language.value),
                               bank_code=str(booking_cr.bank_code.value), order_desc=content, order_id=order_id)
        else:
            response = "SUCCESS"
        return response

    async def payment_return(self, request: Request):
        result = payment_return(request=request)
        ids = result.get('order_desc')
        ids = ids.split(",")
        if result.get("result") == 'success':
            booking.update_bulk_booking(db=self.db, ids=ids, status_payment=True)
            return "SUCCESS"
        else:
            booking.remove_multi(db=self.db, ids=ids)
            return "NOT SUCCESS"



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
            result, count = booking.get_list_bookings(self.db, skip, limit)
            return result, count

    async def get_bookings_sport(self, sport_id: str, date_booking: date, skip: int, limit: int):
        result = booking.get_list_booking_by_sport_id(db=self.db, sport_id=sport_id, date_booking=date_booking,
                                                      skip=skip, limit=limit)
        return result

    async def get_booking_of_user(self, user_id: str, skip: int, limit: int):
        result, count = booking.get_bookings_of_user(db=self.db, user_id=user_id, skip=skip, limit=limit)
        return result, count
