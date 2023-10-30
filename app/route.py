from fastapi import APIRouter

from app.api.endpoint import user, comment, reply_comment


route = APIRouter()

route.include_router(user.router, tags=["users"])
route.include_router(comment.router, tags=["comment"])
route.include_router(reply_comment.router, tags=["reply_comment"])
