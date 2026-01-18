from httpx import AsyncClient


async  def test_full_path_to_inventory(ac:AsyncClient):

    email = "Morkovnik@gmail.com"
    password  = "Mellstroy228"
    status_code = 200
    inventory_id = 11



    login_responce = await  ac.post("/auth/login", json={
        "email": email,
        "password": password
    })

    assert  login_responce.status_code == status_code

    inventory_responce = await  ac.get("/UserInventory")
    assert  inventory_responce.status_code == status_code
    inventory_data = inventory_responce.json()
    assert any(item["user_id"] == 11 for item in inventory_data)



    market_add_responce = await  ac.post("/Market",json={
        "inventory_id": inventory_id,
        "price": 3333
    })
    assert market_add_responce.status_code == 200


    market_upd_responce = await ac.get("/Market")
    assert  market_upd_responce.status_code == 200
    items = market_upd_responce.json()
    assert any(item["inventory_id"] == inventory_id for item in items)

    logout_responce = await  ac.post("/auth/logout")
    assert logout_responce.status_code == status_code

    final_check = await ac.get("/auth/me")
    assert final_check.status_code == 401
