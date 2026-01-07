from sqlalchemy import  select
from sqlalchemy.orm import joinedload

from app.UserInventory.models import UserInventoryModel
from app.dao.base import BaseDao
from app.database import async_session_maker


class InventoryDao(BaseDao):
    model = UserInventoryModel



    @classmethod
    async def find_by_id(cls, model_id:int):
        async  with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id).options(joinedload(cls.model.skin))
            result = await session.execute(query)
            return result.scalar_one_or_none()



