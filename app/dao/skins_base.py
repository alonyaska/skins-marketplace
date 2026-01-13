
from sqlalchemy import select
from sqlalchemy.orm import joinedload


from app.UserInventory.models import UserInventoryModel
from app.dao.base import BaseDao
from app.database import async_session_maker
from app.skins.models import SkinsModel
from app.Market.models import MarketModel

class SkinsBaseDao(BaseDao):


    @classmethod
    async  def get_all_skins(cls):
        async  with  async_session_maker() as session:
            query = select(cls.model)
            result = await session.execute(query)
            print(f"DEBUG: {result}")
            return  result.scalars().all()



    @classmethod
    async def apply_filtres(
            cls,
            user_id:int,
            name: str = None ,
            type_weapon: str =None,
            rarity: str = None,
            min_price: int = None,
            max_price: int = None,
):
     async  with async_session_maker() as session:
         query = select(cls.model)


         if name:
             query = query.filter(cls.model.name.ilike(f"%{name}%"))
         if rarity:
            query = query.filter(cls.model.rarity.ilike(f'%{rarity}%'))
         if min_price is not None:
             query = query.filter(cls.model.price >= min_price)
         if max_price is not None:
             query = query.filter(cls.model.price <= max_price)
         if type_weapon:
             query = query.filter(cls.model.type_weapon.ilike(f"%{type_weapon}%"))
         if user_id is not None:
             query=query.filter(cls.model.id == user_id)


         result = await  session.execute(query)
         return result.scalars().all()




    @classmethod
    async def apply_filters_market(
            cls,
            name: str = None,
            type_weapon: str = None,
            rarity: str = None,
            min_price: int = None,
            max_price: int = None,
            ):

        async with async_session_maker() as session:

            query = select(MarketModel).join(
                MarketModel.item
            ).join(UserInventoryModel.skin)


            if min_price is not None:
                query = query.filter(MarketModel.price >= min_price)
            if max_price is not  None:
                query = query.filter(MarketModel.price <= max_price)

            if name:
                query = query.filter(SkinsModel.name.ilike(f"%{name}%"))
            if rarity:
                query = query.filter(SkinsModel.rarity == rarity)
            if type_weapon:
                query = query.filter(SkinsModel.type_weapon.ilike(f"%{type_weapon}%"))

            query =  query.options(
                joinedload(MarketModel.item).joinedload(UserInventoryModel.skin)
            )

            result = await  session.execute(query)
            return  result.scalars().all()







