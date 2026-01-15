
from sqlalchemy import select, update
from sqlalchemy.orm import joinedload

from app.Market.models import MarketModel
from app.UserInventory.models import UserInventoryModel
from app.Users.models import UsersModel
from app.dao.base import BaseDao
from app.database import async_session_maker
from app.exceptions import InventoryNotFound, SkinAlreadyOnMarket, NotEnoughMoney


class MarketDao(BaseDao):
    model = MarketModel

    @classmethod
    async def get_all_lots(
            cls,
            limit:int,
            offset:int):
        async with async_session_maker() as session:
            query = (
                select(cls.model)
                .options(
                    joinedload(cls.model.item)  # Подгружаем инвентарь
                    .joinedload(UserInventoryModel.skin)  # Пробрасываем до библиотеки скинов
                )
            )
            query = query.limit(limit).offset(offset)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def add(cls, user_id: int, inventory_id: int, price: int):
        async with async_session_maker() as session:
            # 1. Проверки (оставляем как есть)
            query = select(UserInventoryModel).filter_by(id=inventory_id, user_id=user_id)
            result = await session.execute(query)
            item = result.scalar_one_or_none()
            if not item:
                raise InventoryNotFound

            check_query = select(MarketModel).filter_by(inventory_id=inventory_id)
            check_result = await session.execute(check_query)
            if check_result.scalar_one_or_none():
                raise SkinAlreadyOnMarket

            # 2. Создание записи
            new_sale = MarketModel(
                inventory_id=inventory_id,
                seller_id=user_id,
                price=price
            )
            session.add(new_sale)

            # 3. Фиксация в БД
            await session.commit()

            # 4. МАГИЯ ТУТ: Обновляем объект, чтобы в нем появились ID и created_at из БД
            await session.refresh(new_sale)

            # 5. Возвращаем объект в виде словаря (или сам объект)
            # Если у тебя нет метода to_dict(), можно сделать так:
            return {
                "id": new_sale.id,
                "inventory_id": new_sale.inventory_id,
                "seller_id": new_sale.seller_id,
                "price": new_sale.price,
                "created_at": new_sale.created_at  # Если это поле есть в модели
            }

    @classmethod
    async def buy_lot_on_market(cls, buyer_id: int, inventory_id: int):
        async with async_session_maker() as session:
            async with session.begin():
                # 1. Находим лот и блокируем строку (Lock)
                query = select(MarketModel).filter_by(inventory_id=inventory_id).with_for_update()
                result = await session.execute(query)
                market_item = result.scalar_one_or_none()

                if not market_item:
                    raise InventoryNotFound
                if market_item.seller_id == buyer_id:

                    raise SkinAlreadyOnMarket


                buyer = await session.get(UsersModel, buyer_id, with_for_update=True)
                seller = await session.get(UsersModel, market_item.seller_id, with_for_update=True)

                if buyer.balance < market_item.price:
                    raise NotEnoughMoney


                deal_data = {
                    "inventory_id": market_item.inventory_id,
                    "price": market_item.price,
                    "seller_id": market_item.seller_id,
                    "buyer_id": buyer_id,
                    "buyer_new_balance": buyer.balance - market_item.price
                }


                buyer.balance -= market_item.price
                seller.balance += market_item.price


                update_inv_query = (
                    update(UserInventoryModel)
                    .where(UserInventoryModel.id == inventory_id)
                    .values(user_id=buyer_id)
                )
                await session.execute(update_inv_query)


                await session.delete(market_item)


                return deal_data

