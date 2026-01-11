


import  random
from fastapi import  FastAPI, Query,HTTPException,  Depends
from typing import Optional
from  datetime import  date
from pydantic import BaseModel
from starlette.status import HTTP_403_FORBIDDEN, HTTP_422_UNPROCESSABLE_CONTENT
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


class SkinsArgSearch:
    def __init__(
            self,
            rarity: Optional[int] = Query(None, ge =1, le= 3),
            max_price:Optional[int] = Query(None, ge = 1, le = 150000),
    ):
        self.rarity = rarity
        self.max_price = max_price



class Sskin(BaseModel):
    name:str
    rarity:int
    price:int


class SListing(BaseModel):
    skin_id:int
    seller_name:str
    data_sell: date



class Snewyear(BaseModel):
    pozdr:str
    positive:bool

@app.get("/newyear26", response_model=Snewyear)
def happy_newyear(
        is_positive_vibe: Optional[bool] =None
):
    wishes = [
        "Твой код будет работать с первого раза!",
        "Оффер в Питере уже ждет тебя!",
        "31/11 в каждой катке 2026 года!"
    ]
    return {
        "pozdr": random.choice(wishes) if is_positive_vibe else "Просто отдохни, бро.",
        "positive": is_positive_vibe
    }


@app.get("/skins", response_model=list[Sskin])
def get_skins(
        search_args: SkinsArgSearch = Depends()
):
    skins = [
        {
            "name": "AK-47 Redline",
            "rarity": 2,
            "price": 6999,

        }
    ]

    return skins

@app.post("/sell")
def sell_skin(selling:SListing):
    if selling.seller_name == "Scammer":
        raise  HTTPException(
            status_code=HTTP_403_FORBIDDEN,
            detail="Вам запрещено торговать на площадке"
        )
    if selling.skin_id < 0:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_CONTENT,
            detail="Неверный ID предмета"
        )
    pass
    return  {
        "status":  "Предмет выставлен",
        "data": selling
    }





