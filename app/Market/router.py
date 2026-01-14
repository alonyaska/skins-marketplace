import asyncio

from fastapi import APIRouter, Depends, Query
from fastapi_cache.decorator import cache

from app.Market.dao import MarketDao
from app.Market.service import MarketService
from app.Users.dependencies import get_current_user
from app.Users.models import UsersModel

router = APIRouter(
    prefix="/Market",
    tags = ["Маркет"]
)




@router.get("")
@cache(expire=60)
async  def get_all_market(
        limit:int =  Query(10, ge=1, le=100),
        offset:int = Query(0, ge=0)
):
    return  await MarketService.get_all_market_or_404(
        limit=limit,
        offset=offset
    )


@router.post("")
async def  add_skin_on_market(
            inventory_id:int,
            price:int,
        user: UsersModel = Depends(get_current_user)
):
    await  MarketDao.add(user.id, inventory_id, price)



@router.post("/buy")
async  def buy_skin_on_market(
        inventory_id: int,
        user: UsersModel = Depends(get_current_user)
):
    await  MarketDao.buy_lot_on_market(buyer_id=user.id, inventory_id=inventory_id)


@router.get("/filter")
@cache(expire=60)
async def filter_market(
        name: str = None,
        rarity: str = None,
        type_weapon:str = None,
        min_price: int = None,
        max_price: int = None
):
    return  await MarketService.get_all_filtered_market(
        name=name,
        rarity=rarity,
        type_weapon=type_weapon,
        min_price=min_price,
        max_price=max_price
    )