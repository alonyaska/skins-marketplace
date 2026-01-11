from fastapi import APIRouter, Depends

from app.Market.dao import MarketDao
from app.Market.service import MarketService
from app.Users.dependencies import get_current_user
from app.Users.models import UsersModel

router = APIRouter(
    prefix="/Market",
    tags = ["Маркет"]
)




@router.get("")
async  def get_all_market():
    return  await MarketService.get_all_market_or_404()


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