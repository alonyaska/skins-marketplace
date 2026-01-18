import pytest
from httpx import AsyncClient



@pytest.mark.parametrize("user,email,password,status_code", [
    ("alonyaTEST", "alonya@test.com", "12345", 200),
    ("alonyaskaTEST", "alonyaska@test.com", "123456", 200),
    ("alonchikTEST", "Morkovnik@gmail.com", "233231", 401)


]
                         )
async def test_register_user(user,email,password,status_code,ac: AsyncClient):
    responce =await  ac.post("/auth/register", json={
        "user": user,
        "email": email,
        "password": password
    })

    assert  responce.status_code == status_code





@pytest.mark.parametrize("email,password, status_code", [
    ("Morkovnik@gmail.com","Mellstroy228", 200),
    ("alonya@mail.ru", "1231231", 401)

])
async def test_login_user(email, password,status_code, ac:AsyncClient):
    responce =await  ac.post("/auth/login", json={
        "email":email,
        "password":password
    })
    assert  responce.status_code == status_code

