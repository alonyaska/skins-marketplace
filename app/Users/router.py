from fastapi import APIRouter



from app.Users.schemas import SUserRegister
from app.Users.service import UsersService

router = APIRouter(
    prefix="/auth",
    tags=["Auth and Users"]

)



@router.post("/register")
async  def register_user(user_data:SUserRegister):
   return  await UsersService.register_or_418(user_data)
