from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from sqladmin import Admin,ModelView
from fastapi import  FastAPI
from fastapi_cache import FastAPICache
from starlette.middleware.cors import CORSMiddleware

from app.UserInventory.router import router as router_inventory
from app.admin.auth import authentication_backend
from app.admin.views import UserAdmin, UserInventAdmin, SkinsModelAdmin, MarketModelAdmin
from app.database import engine
from  app.skins.router import router as router_skins
from app.Users.models import UsersModel
from app.Users.router import router as router_users
from app.Market.router import router as router_market
from  app.pages.router import router as router_pages
from  fastapi.staticfiles import StaticFiles
from  app.images.router import router as router_images
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from app.config import settings

from redis import asyncio as aioredis

@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}")
    FastAPICache.init(RedisBackend(redis), prefix="cache")
    yield




app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="app/static"), "static")

app.include_router(router_users)
app.include_router(router_market)
app.include_router(router_images)
app.include_router(router_pages)
app.include_router(router_inventory)
app.include_router(router_skins)


origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET","POST","PATH","DELETE","PUT"],
    allow_headers = ["*"] # но лучше прописывать ради безапасности

)

admin = Admin(app, engine, authentication_backend=authentication_backend)





admin.add_view(UserAdmin)
admin.add_view(UserInventAdmin)
admin.add_view(SkinsModelAdmin)
admin.add_view(MarketModelAdmin)









