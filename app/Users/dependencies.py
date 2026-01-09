from datetime import datetime

from fastapi import Request, HTTPException
from fastapi.params import Depends
from jose import jwt, JWTError

from app.Users.dao import UsersDao
from app.config import settings


def get_token(request: Request):
    token = request.cookies.get("user_inventory_token")
    if not  token:
        raise  HTTPException(status_code=401, detail="Not Authorized")
    return token



async def  get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )

    except JWTError:
        raise HTTPException(status_code=401, detail="lol nety jwt")
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise HTTPException(status_code=401, detail="jwt istek")
    user_name: str = payload.get("username")
    if not user_name:
        raise HTTPException(status_code=401)
    user = await  UsersDao.find_by_name(user_name)
    if not  user:
        raise HTTPException(status_code=401)

    return  user

