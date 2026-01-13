from fastapi import Query

from app.Market.dao import MarketDao
from app.exceptions import InventoryNotFound
from app.skins.dao import SkinsDao


class MarketService:



    @classmethod
    async  def get_all_market_or_404(cls, **filter_by):
        result =  await MarketDao.get_all_lots()
        if not result:
            raise  InventoryNotFound()
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



