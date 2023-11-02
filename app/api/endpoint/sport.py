from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session


from app.api.depend.user import login_required
from app.api.response.response import make_response_json
from app.api.response.response import make_response_json_4_param
from app.db.database import get_db
from app.schemas.sport import SportCreate
from app.schemas.sport import SportUpdate
from app.services.sport import sport

router = APIRouter()


@router.get("/sport/create")
async def create_sport(post: SportCreate, token: dict = Depends(login_required), db:Session = Depends(get_db)):
    uuid = token['uuid']
    sport_svr = sport(db)
    result = sport_svr.create_sport(post, uuid)
    return make_response_json(data=result, status=200, message="create success")

@router.get("/sport/getall")
def get_spost_all(db: Session = Depends(get_db)):
    service = sport(db=db)
    result = service.get_all()
    return {
        "status": 200,
        "data": result
    }

@router.put("/sport/update")
def update_sport(post_update:SportUpdate, db:Session= Depends(get_db)):
    service = sport(db=db)
    response = service.update_sport(post_cr=post_update)
    return make_response_json(data=response, status=200, message="update thanh cong")

@router.delete("/sport/delete")
def delete_sport(id_post: str, db:Session = Depends(get_db)):
    service = sport(db=db)
    response = service.remove_sport(post_id=id_post)
    return make_response_json(data="", status=200, message="delete success")