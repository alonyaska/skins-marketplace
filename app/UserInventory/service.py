


from app.UserInventory.dao import InventoryDao
from app.exceptions import InventoryNotFound


class InventoryService:


        @classmethod
        async def get_by_id_or_404(cls, model_id:int):
            result = await InventoryDao.find_by_id(model_id)
            if not result:
                raise InventoryNotFound
            return result



        @classmethod
        async  def find_all_or_404(cls, **filter_by):
            result = await InventoryDao.get_all(**filter_by)
            if not result:
                raise InventoryNotFound
            return result



        @classmethod
        async def  get_inventory_or_404(cls):
            result = await InventoryDao.get_all_with_details()
            if not result:
                raise InventoryNotFound
            return result
