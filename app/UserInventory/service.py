from fastapi import HTTPException


from app.UserInventory.dao import InventoryDao


class InventoryService:


        @classmethod
        async def get_by_id_or_404(cls, model_id:int):
            result = await InventoryDao.find_by_id(model_id)
            if not result:
                raise HTTPException(status_code=404, detail="Inventory not found")
            return result


        @classmethod
        async def  get_inventory_or_404(cls):
            result = await InventoryDao.get_all_with_details()
            if not result:
                raise HTTPException(status_code=404, detail="Item or User not found")
            return result
