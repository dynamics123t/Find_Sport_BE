import cloudinary
from cloudinary import uploader
from fastapi import APIRouter, UploadFile, File
from fastapi import Depends
from sqlalchemy.orm import Session

from app.api.depend.user import login_required
from app.api.response.response import make_response_json
from app.api.response.response import make_response_json_4_param
from app.db.database import get_db
from app.schemas.sport import SportCreate
from app.schemas.sport import SportUpdate
from ..depend import oauth2
from ...model import User
from ...schemas import SportBase
from ...services import PostService

router = APIRouter()


@router.post("/sport/create")
async def create_sport(post: SportBase, user: User = Depends(oauth2.admin),
                       db: Session = Depends(get_db)):
    sport_svr = PostService(db=db)
    breakpoint()
    result = sport_svr.create_sport(post, user.id)
    return make_response_json(data=result, status=200, message="create success")


@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    result = cloudinary.uploader.upload(file.file, folder="sport")
    return result.get("secure_url")


@router.get("/sport/get_all")
def get_sport_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    service = PostService(db=db)
    result = service.get_all(skip=skip, limit=limit)
    return {
        "status": 200,
        "data": result
    }


@router.put("/sport/{sport_id}/update")
def update_sport(sport_id: str, post_update: SportUpdate, user: User = Depends(oauth2.admin),
                 db: Session = Depends(get_db)):
    service = PostService(db=db)
    response = service.update_sport(sport_id=sport_id, sport_update=post_update)
    return make_response_json(data=response, status=200, message="update thanh cong")


@router.delete("/sport/{sport_id}/delete")
def delete_sport(sport_id: str, db: Session = Depends(get_db), user: User = Depends(oauth2.admin)):
    service = PostService(db=db)
    response = service.remove_sport(sport_id=sport_id)
    return make_response_json(data="", status=200, message="delete success")


@router.get("/sport/me")
def get_sport_of_me(name: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    service = PostService(db=db)
    response, count = service.get_sport_of_me(name=name, skip=skip, limit=limit)
    return make_response_json_4_param(data=response, count=count, status=200, message="thanh cong")
