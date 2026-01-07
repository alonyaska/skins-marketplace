from pydantic import BaseModel, EmailStr


class SUserRegister(BaseModel):
    user: str
    email:EmailStr
    password:str