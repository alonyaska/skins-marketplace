
from sqlalchemy import select

from app.dao.base import BaseDao
from app.database import async_session_maker


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
            name: str = None ,
            rarity: str = None,
            min_price: int = None,
            max_price: int = None,
):
     async  with async_session_maker() as session:
         query = select(cls.model)


         if name:
             query = query.filter(cls.model.name.ilike(f"%{name}%"))
         if rarity:
            query = query.filter(cls.model.rarity.ilike(f'%{rarity}'))
         if min_price is not None:
             query = query.filter(cls.model.price >= min_price)
         if max_price is not None:
             query = query.filter(cls.model.price <= max_price)


         result = await  session.execute(query)
         return result.scalars().all()