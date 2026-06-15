from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from dependencies import get_db
from sqlalchemy.orm import Session
from jwt_config import SECRET_KEY,ALGORITHM
from jose import jwt
from models import User

oauth2_scheme=OAuth2PasswordBearer(
    tokenUrl="login"
)

def get_current_user(
        token:str=Depends(oauth2_scheme),
        db:Session=Depends(get_db)
):
    payload=jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )
    username=payload.get("sub")
    user=(
        db.query(User)
        .filter(User.username == username)
        .first()
    )
    return user