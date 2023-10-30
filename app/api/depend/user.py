import logging

import jwt
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session

from app.core.settings import settings
from app.crud.user import crud_user
from app.db.database import get_db
from app.model.user import User

logger = logging.getLogger(__name__)


def login_required(http_authorization_credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False)),
                   db: Session = Depends(get_db)):
    if http_authorization_credentials is None:
        raise HTTPException(
            status_code=401,
            detail="UNAUTHORIZED",
            headers={'WWW-Authenticate': 'Bearer realm="auth_required"'},
        )
    try:
        decoded_token = jwt.decode(http_authorization_credentials.credentials, settings.SECRET_KEY,
                                   algorithms=["HS256"])
        uid = decoded_token['uid']
        db_user = crud_user.get(db=db, id=uid)

        if db_user is None:
            raise HTTPException(
                status_code=401,
                detail="UNAUTHORIZED"
            )
        return decoded_token
    except Exception as err:
        logger.info("Service: Exception.", exc_info=err)
        raise HTTPException(
            status_code=401,
            detail="LOGIN ko thanh cong"
        )


def get_current_user(
        token: dict = Depends(login_required),
        db: Session = Depends(get_db)
):
    uid = token['uid']
    db_user = crud_user.get(db=db, id=uid)

    if db_user is None:
        raise HTTPException(
            status_code=401,
            detail="Authorization Failed"
        )

    return db_user


def get_current_user_active(
        token: dict = Depends(login_required),
        db: Session = Depends(get_db)
):
    uid = token['uid']
    db_user = crud_user.get(db=db, id=uid)

    if db_user is None:
        raise HTTPException(
            status_code=401,
            detail="Authorization Failed"
        )
    if not db_user.is_activate:
        raise HTTPException(
            status_code=401,
            detail="Account is not active"
        )
    return db_user


def user_admin(current_user: User = Depends(get_current_user)) -> User:
    if not crud_user.is_active(current_user) or not current_user.is_super:
        raise HTTPException(status_code=401, detail="Inactive user")
    return current_user