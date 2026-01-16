from fastapi import Query

from app.UserInventory.dao import InventoryDao
from app.UserInventory.models import UserInventoryModel
from app.UserInventory.schemas import SUserInventory
from app.Users.service import UsersService
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
        async def  get_inventory_or_404(cls, **filter_by):
            result = await InventoryDao.get_all(**filter_by)
            if not result:
                raise InventoryNotFound
            return result

        @classmethod
        async def filtered_inventory(
                cls,
                user_id:int,
                name: str = None,
                rarity: str = None,
                type_weapon: str = None
        )-> list[SSkins]:
            return  await SkinsDao.apply_filter_inventory(
                user_id=user_id,
                name=name,
                rarity=rarity,
                type_weapon=type_weapon
            )

