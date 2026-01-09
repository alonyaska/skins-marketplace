from fastapi import APIRouter, Response, Depends

from app.UserInventory.schemas import SUserInventory
from app.Users.dependencies import get_current_user
from app.Users.schemas import SUserRegister, SUserLogin
from app.Users.service import UsersService

router = APIRouter(
    prefix="/auth",
    tags=["Auth and Users"]

)



@router.post("/register")
async  def register_user(user_data:SUserRegister):
   return  await UsersService.register_or_418(user_data)



@router.post("/login")
async def login_user(user_data:SUserLogin, response: Response):
    return  await UsersService.login_or_401(user_data, response)


@router.post("/logout")
async  def logout_user(response: Response):
    return  await UsersService.logout_or_401(response)


@router.get("/me")
async  def  read_users_me(currrent_user: SUserInventory = Depends(get_current_user)):
    return currrent_user
