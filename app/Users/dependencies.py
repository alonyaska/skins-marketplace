from datetime import datetime

from fastapi import Request
from fastapi.params import Depends
from jose import jwt, JWTError

from app.Users.dao import UsersDao
from app.config import settings
from app.exceptions import UserNotLogInException, TokenAbsentException, TokenIsExpireException, IncorrectTokenType


def get_token(request: Request):
    token = request.cookies.get("user_inventory_token")
    if not  token:
        raise  UserNotLogInException
    return token



async def  get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )

    except JWTError:
        raise TokenAbsentException
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenIsExpireException
    user_name: str = payload.get("username")
    if not user_name:
        raise IncorrectTokenType
    user = await  UsersDao.find_by_name(user_name)
    if not  user:
        raise IncorrectTokenType

    return  user

