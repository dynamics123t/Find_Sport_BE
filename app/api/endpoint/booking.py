from datetime import date

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.depend import oauth2
from app.api.response.response import make_response_json_4_param
from app.db.database import get_db
from app.model import User
from app.model.base import StatusBookingEnum
from app.schemas.booking import BookingBase, BookingUpdate
from app.services.booking import BookingService
from app.utils.response import make_response_object

router = APIRouter()


@router.post("/booking/create")
async def create_booking(booking: BookingBase, db: Session = Depends(get_db),
                         user: User = Depends(oauth2.get_current_active_user)):
    service = BookingService(db=db)
    result = await service.create_booking(request=booking, user_id=user.id)
    return make_response_object(result)


@router.get('/booking')
async def get_booking(booking_id: str = None, skip: int = 0, limit: int = 10, db: Session = Depends(get_db),
                      user: User = Depends(oauth2.get_current_active_user)):
    service = BookingService(db=db)
    result, count = await service.get_booking(booking_id=booking_id, skip=skip, limit=limit)
    return make_response_json_4_param(data=result, count=count, status=200, message="Success")


@router.get("/booking/user")
async def get_booking_of_user(skip: int = 0, limit: int = 10, db: Session = Depends(get_db),
                              user: User = Depends(oauth2.get_current_active_user)):
    service = BookingService(db=db)
    result, count = await service.get_booking_of_user(user_id=user.id, skip=skip, limit=limit)
    return make_response_json_4_param(data=result, count=count, status=200, message="success")


@router.get('/booking/sport')
async def get_booking_of_sport(sport_id: str, date_booking: date, skip: int = 0, limit: int = 10,
                               db: Session = Depends(get_db),
                               user: User = Depends(oauth2.get_current_active_user)):
    service = BookingService(db=db)
    result, count = await service.get_bookings_sport(sport_id=sport_id, date_booking=date_booking, skip=skip,
                                                     limit=limit)
    return make_response_json_4_param(data=result, count=count, status=200, message="Success")


@router.put('/booking/{booking_id}/status')
async def get_booking(booking_id: str, status: StatusBookingEnum, db: Session = Depends(get_db),
                      user: User = Depends(oauth2.get_current_active_user)):
    service = BookingService(db=db)
    result = await service.update_status(booking_id=booking_id, status=status)
    return make_response_object(result)


@router.put('/booking/{booking_id}')
async def get_booking(booking_id: str, booking_update: BookingUpdate, db: Session = Depends(get_db),
                      user: User = Depends(oauth2.get_current_active_user)):
    service = BookingService(db=db)
    result = await service.update_scheduler_booking(booking_id=booking_id, request=booking_update)
    return make_response_object(result)
