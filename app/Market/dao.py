from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.Market.models import MarketModel
from app.UserInventory.models import UserInventoryModel
from app.dao.base import BaseDao
from app.database import async_session_maker


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