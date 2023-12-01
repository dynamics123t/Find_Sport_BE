from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.booking import BookingService
from app.utils.vnpay import Vnpay
from app.api.response.response import make_response_json
from app.api.response.response import make_response_json_4_param
from datetime import datetime
from app.constant.app_status import AppStatus
from app.core.exceptions import error_exception_handler
from app.core.settings import settings
from app.utils.vnpay import Vnpay

router = APIRouter()

@router.get("/payment_return")
async def payment_return(request: Request, db:Session =Depends(get_db)):
    service = BookingService(db=db)
    return RedirectResponse(url='http://localhost:3000/sports/bongda')