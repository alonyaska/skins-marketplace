from fastapi import Query

from app.UserInventory.dao import InventoryDao
from app.UserInventory.schemas import SUserInventory
from app.exceptions import InventoryNotFound
from app.skins.dao import SkinsDao
from app.skins.sсhemas import SSkins


class InventoryService:


        @classmethod
        async def get_by_id_or_404(cls, model_id:int):
            result = await InventoryDao.find_by_id(model_id)
            if not result:
                raise InventoryNotFound()
            return result



        @classmethod
        async  def find_all_or_404(cls, **filter_by):
            result = await InventoryDao.get_all(**filter_by)
            if not result:
                raise InventoryNotFound()
            return result



        @classmethod
        async def  get_inventory_or_404(cls):
            result = await InventoryDao.get_all_with_details()
            if not result:
                raise InventoryNotFound
            return result

        @classmethod
        async def filtered_inventory(
                cls,
                user_id:int,
                name: str = Query(None, description="Поиск по названию"),
                rarity: str = Query(None, description="Фильтр по редкости"),
                type_weapon: str = Query(None, description="Фильтр по типу Оружия"),
                min_price: int = Query(None, description="Минимальная цена"),
                max_price: int = Query(None, description="Максимальная цена")
        )-> list[SSkins]:
            return  await SkinsDao.apply_filtres(
                user_id=user_id,
                name=name,
                rarity=rarity,
                type_weapon=type_weapon,
                min_price=min_price,
                max_price=max_price
            )
