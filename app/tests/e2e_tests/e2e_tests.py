import  pytest
from httpx import  AsyncClient


async  def test_full_user_path(ac:AsyncClient):

    user = "e2eclient"
    email = "e2etest@test.com"
    password = "12345678"
    status_code = 200


    register_responce =await  ac.post("/auth/register", json={
        "user": user,
        "email": email,
        "password": password
    })
    assert register_responce.status_code == status_code


    login_responce = await  ac.post("/auth/login", json={
        "email": email,
        "password": password
    })
    assert login_responce.status_code == status_code


    auth_responce = await  ac.get("/auth/me")
    assert  auth_responce.status_code == status_code
    assert  auth_responce.json()["email"] ==  email


    deposit_responce = await  ac.post("/auth/deposit", json={
        "deposit": 5000
    })
    assert  deposit_responce.status_code == status_code

    me_responce = await ac.get("/auth/me")
    assert  me_responce.json()["balance"] == 4750



    buy_responce = await ac.post("/Market/buy", json={
        "inventory_id":10
    })
    assert   buy_responce.status_code == status_code



    logout_responce = await  ac.post("/auth/logout")
    assert logout_responce.status_code == status_code

    final_check = await ac.get("/auth/me")
    assert final_check.status_code == 401




