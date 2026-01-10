
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.Market.models import MarketModel
from app.UserInventory.models import UserInventoryModel
from app.dao.base import BaseDao
from app.database import async_session_maker
from app.exceptions import InventoryNotFound, SkinAlreadyOnMarket


class MarketDao(BaseDao):
    model = MarketModel

    @classmethod
    async def get_all_lots(cls):
        async with async_session_maker() as session:
            query = (
                select(cls.model)
                .options(
                    joinedload(cls.model.item)  # Подгружаем инвентарь
                    .joinedload(UserInventoryModel.skin)  # Пробрасываем до библиотеки скинов
                )
            )
            result = await session.execute(query)
            return result.scalars().all()



    @classmethod
    async  def add(
            cls,
            user_id:int,
            inventory_id:int,
            price:int
    ):
        async  with async_session_maker() as session:
            query =  select(UserInventoryModel).filter_by(id=inventory_id, user_id=user_id)
            result = await  session.execute(query)
            item = result.scalar_one_or_none()
            if not item:
                raise  InventoryNotFound

            check_query = select(MarketModel).filter_by(inventory_id = inventory_id)
            check_result = await  session.execute(check_query)
            if check_result.scalar_one_or_none():
                raise SkinAlreadyOnMarket

            new_sale = MarketModel(
                inventory_id = inventory_id,
                seller_id = user_id,
                price = price
            )
            session.add(new_sale)
            await  session.commit()

            return {"status": "succes"}
