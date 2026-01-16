
from fastapi import Query

from app.Market.dao import MarketDao
from app.exceptions import InventoryIsNull
from app.skins.dao import SkinsDao


class MarketService:



    @classmethod
    async  def get_all_market_or_404(
            cls,
            limit:int,
            offset:int
        ):
        result =  await MarketDao.get_all_lots(
            limit=limit,
            offset=offset
        )
        if not result:
            raise  InventoryIsNull()
        return  result



    @classmethod
    async  def get_all_filtered_market(
            cls,
            name: str = Query(None, description="Поиск по названию"),
            rarity: str = Query(None, description="Фильтр по редкости"),
            type_weapon: str = Query(None, description="Фильтр по типу Оружия"),
            min_price: int = Query(None, description="Минимальная цена"),
            max_price: int = Query(None, description="Максимальная цена")
    ):
        return  await SkinsDao.apply_filters_market(
            name=name,
            rarity=rarity,
            type_weapon=type_weapon,
            min_price=min_price,
            max_price=max_price
        )


    @classmethod
    async  def delete_lot_market(
            cls,
            lot_id:int,
            user_id:int
                                 ):

        return  await MarketDao.delete_market_lot(
            user_id=user_id,
            lot_id=lot_id
        )



