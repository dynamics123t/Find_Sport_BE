from fastapi import APIRouter

from app.api.endpoint import user, comment, reply_comment, sport, contact, booking,payment
route = APIRouter()

route.include_router(user.router, tags=["users"])
route.include_router(comment.router, tags=["comment"])
route.include_router(reply_comment.router, tags=["reply_comment"])
route.include_router(sport.router, tags=["sport"])
route.include_router(contact.router, tags=["contact"])
route.include_router(booking.router, tags=["booking"])
route.include_router(payment.router, tags=["payment"])