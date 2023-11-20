import datetime
from datetime import date
from typing import Optional, List

from pydantic import BaseModel

from app.model.base import TimeBookingEnum, ModeOfPaymentEnum


class BookingBase(BaseModel):
    id_sport: Optional[str] = None
    time: Optional[List[TimeBookingEnum]] = [TimeBookingEnum.TIME_5H]
    date: Optional[date] = None
    mode_of_payment: Optional[ModeOfPaymentEnum] = ModeOfPaymentEnum.CASH
    payment_status: Optional[bool] = False

    class Config:
        orm_mode = True

    def custom_dict(self):
        return dict(id_sport=self.id_sport, date=self.date, mode_of_payment=self.mode_of_payment,
                    payment_status=self.payment_status)


class BookingCreate(BookingBase):
    id: Optional[str] = None
    id_user: Optional[str] = None
    time: Optional[TimeBookingEnum] = TimeBookingEnum.TIME_5H


class BookingUpdate(BaseModel):
    id_sport: Optional[str] = None
    time: Optional[str] = None
    date: Optional[date] = None
