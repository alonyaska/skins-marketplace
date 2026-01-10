from pydantic import BaseModel, EmailStr


class SUserRegister(BaseModel):
    user: str
    email:EmailStr
    password:str



class SUserLogin(BaseModel):
    email: EmailStr
    password:str


class SUsers(BaseModel):
    id: int
    user:str

