import json
from datetime import datetime

import pytest
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend

from sqlalchemy import insert

from app.config import settings
from app.database import Base, async_session_maker,engine
from app.Users.models import UsersModel
from app.skins.models import SkinsModel
from app.UserInventory.models import UserInventoryModel
from app.Market.models import  MarketModel

from app.main import app

from  fastapi.testclient import TestClient
from httpx import AsyncClient, ASGITransport

from app.tasks.celerys import celery


@pytest.fixture(scope="session",autouse=True)
async def prepare_database():
    FastAPICache.init(InMemoryBackend())
    assert settings.MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


    def open_mock_json(model:str):
        with open(f"app/tests/mock_to_{model}.json", "r", encoding="utf-8") as file:
            return  json.load(file)


    users = open_mock_json("users")
    skins = open_mock_json("skins")
    inventory = open_mock_json("inventory")
    market = open_mock_json("market")

    for item in market:
        item["created_at"] = datetime.strptime(item["created_at"],"%Y-%m-%d")


    async  with async_session_maker() as session:
        add_users = insert(UsersModel).values(users)
        add_skins = insert(SkinsModel).values(skins)
        add_inventory = insert(UserInventoryModel).values(inventory)
        add_market = insert(MarketModel).values(market)

        await  session.execute(add_users)
        await  session.execute(add_skins)
        await  session.execute(add_inventory)
        await  session.execute(add_market)


        await  session.commit()


@pytest.fixture(scope="function")
async  def ac():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield  ac



@pytest.fixture(scope="function")
async def session():
    async with async_session_maker() as session:
        yield  session

@pytest.fixture(scope="session", autouse=True)
def setup_celery():
    celery.conf.update(task_always_eager=True)
    celery.conf.update(task_eager_propagates=True)

