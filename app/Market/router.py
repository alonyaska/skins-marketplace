

from fastapi import APIRouter, Depends, Query, Body
from fastapi_cache.decorator import cache
from pydantic import TypeAdapter

from app.Market.dao import MarketDao
from app.Market.schemas import SMarket, SBuyResult
from app.Market.service import MarketService
from app.Users.dependencies import get_current_user
from app.Users.models import UsersModel

from app.tasks.tasks import send_market_confirm, send_buy_confirm

router = APIRouter(
    prefix="/Market",
    tags = ["Маркет"]
)


market_adapter = TypeAdapter(SMarket)
buy_adapter = TypeAdapter(SBuyResult)

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


from fastapi import HTTPException, status

@router.post("")
async def add_skin_on_market(
        inventory_id: int = Body(..., embed=True),
        price: int = Body(..., embed=True),
        user: UsersModel = Depends(get_current_user)
):

    if price <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Цена должна быть больше нуля"
        )

    add_market = await MarketDao.add(
        user_id=user.id,
        inventory_id=inventory_id,
        price=price
    )


    if not add_market:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Предмет не найден или не принадлежит вам"
        )


    try:
        add_market_dict = market_adapter.validate_python(add_market).model_dump()
        send_market_confirm.delay(add_market_dict, user.email)
        return add_market_dict
    except Exception as e:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ошибка обработки данных: {str(e)}"
        )

@router.post("/buy")
async  def buy_skin_on_market(
        inventory_id: int = Body(..., embed=True),
        user: UsersModel = Depends(get_current_user)
):
    buy_skin = await  MarketDao.buy_lot_on_market(buyer_id=user.id, inventory_id=inventory_id)
    buy_skin_dict = buy_adapter.validate_python(buy_skin).model_dump()
    send_buy_confirm(buy_skin_dict, user.email)
    return


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

@router.delete("")
async  def delete_lot(
        lot_id:int = Query(None, description="айди лота для удаления"),
        user: UsersModel = Depends(get_current_user),

):
    return  await MarketService.delete_lot_market(
        lot_id=lot_id,
        user_id = user.id
    )