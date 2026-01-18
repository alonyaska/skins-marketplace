
from  httpx import  AsyncClient



async def test_full_wrong_path(ac:AsyncClient):
    user = "testclient"
    email = "Best.test.com"
    password = "123456718"
    status_code = 200



    register1_responce = await  ac.post("/auth/register", json={
        "user": user,
        "email": email,
        "password": password
    })
    assert register1_responce.status_code != status_code


    email = "Best@test.com"

    register2_responce = await  ac.post("/auth/register", json={
        "user": user,
        "email": email,
        "password": password
    })
    assert register2_responce.status_code == status_code

    login1_responce = await  ac.post("/auth/login", json={
        "email": email,
        "password": 123
    })
    assert login1_responce.status_code != status_code

    login2_responce = await  ac.post("/auth/login", json={
        "email": email,
        "password": password
    })
    assert login2_responce.status_code == status_code

    deposit_responce1 = await  ac.post("/auth/deposit", json={
        "deposit": -500
    })
    assert deposit_responce1.status_code != status_code

    deposit_responce = await  ac.post("/auth/deposit", json={
        "deposit": 5000
    })
    assert deposit_responce.status_code == status_code

    me_responce = await ac.get("/auth/me")
    assert me_responce.json()["balance"] == 4750

    buy_responce = await ac.post("/Market/buy", json={
        "inventory_id": 10
    })
    assert buy_responce.status_code != status_code

    market_add_responce = await  ac.post("/Market", json={
        "inventory_id": 10,
        "price": -3333
    })
    assert market_add_responce.status_code != 200

    logout_responce = await  ac.post("/auth/logout")
    assert logout_responce.status_code == status_code

    final_check = await ac.get("/auth/me")
    assert final_check.status_code == 401













