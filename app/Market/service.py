from app.Market.dao import MarketDao
from app.exceptions import InventoryNotFound


class MarketService:



    @classmethod
    async  def get_all_market_or_404(cls, **filter_by):
        result =  await MarketDao.get_all_lots()
        if not result:
            raise  InventoryNotFound()
        return  result


