from Demos.win32ts_logoff_disconnected import username
from sqlalchemy import  select, insert

from sqlalchemy.orm import joinedload

from app.database import async_session_maker



class BaseDao:

    model = None


    @classmethod
    async  def get_all_with_details(cls, **filter_by):
        async  with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by).options(joinedload(cls.model.skin))
            result = await session.execute(query)
            return  result.scalars().all()



    @classmethod
    async  def find_by_id(cls, model_id:int):
        async  with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return  result.scalar_one_or_none()


    @classmethod
    async def find_by_name(cls, model_name:str):
        async  with async_session_maker() as session:
            query = select(cls.model).filter_by(username=model_name)
            result = await  session.execute(query)
            return  result.scalar_one_or_none()



    @classmethod
    async  def get_one_or_none(cls, **filter_by):
        async  with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result =  await  session.execute(query)
            return  result.scalar_one_or_none()





    @classmethod
    async def get_all(cls, **filter_by):
        async with  async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by).options(joinedload(cls.model.skin))
            result = await session.execute(query)
            return result.scalars().all()



    @classmethod
    async def add(cls, **data):
        async  with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await  session.execute(query)
            await  session.commit()
