from fastapi import APIRouter

from app.Market.service import MarketService

router = APIRouter(
    prefix="/Market",
    tags = ["Маркет"]
)




@router.get("")
async  def get_all_market():
    return  await MarketService.get_all_market_or_404()