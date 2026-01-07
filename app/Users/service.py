from fastapi import HTTPException

from app.Users.auth import get_password_hash
from app.Users.dao import UsersDao
from app.Users.schemas import SUserRegister


class UsersService:



    @classmethod
    async def register_or_418(cls, user_data:SUserRegister):
        existing_user = await UsersDao.get_one_or_none(email=user_data.email)
        if existing_user:
            raise HTTPException(status_code=418, detail="User already register on site")
        hashed_password = get_password_hash(user_data.password)
        await  UsersDao.add(username=user_data.user, email=user_data.email, hashed_password=hashed_password)