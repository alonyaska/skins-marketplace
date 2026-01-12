


from fastapi import  FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.UserInventory.router import router as router_inventory
from  app.skins.router import router as router_skins
from app.Users.models import UsersModel
from app.Users.router import router as router_users
from app.Market.router import router as router_market
from  app.pages.router import router as router_pages
from  fastapi.staticfiles import StaticFiles
from  app.images.router import router as router_images




app = FastAPI()

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







