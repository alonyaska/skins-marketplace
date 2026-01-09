from fastapi import HTTPException, Response

from app.Users.auth import get_password_hash, authenticate_user, create_access_token
from app.Users.dao import UsersDao
from app.Users.schemas import  SUserRegister, SUserLogin


class UsersService:



    @classmethod
    async def register_or_418(cls, user_data:SUserRegister):
        existing_user = await UsersDao.get_one_or_none(email=user_data.email)
        if existing_user:
            raise HTTPException(status_code=418, detail="User already register on site")
        hashed_password = get_password_hash(user_data.password)
        await  UsersDao.add(username=user_data.user, email=user_data.email, hashed_password=hashed_password)




    @classmethod
    async def login_or_401(cls, user_data:SUserLogin, response = Response):
        user = await authenticate_user(user_data.email, user_data.password)
        if not user:
            raise  HTTPException(status_code=401   , detail="User not Auth")
        access_token = create_access_token({"sub": str(user.id),
                                           "username": user.username})
        response.set_cookie("user_inventory_token", access_token, httponly=True, secure=False,samesite="lax")
        return access_token
