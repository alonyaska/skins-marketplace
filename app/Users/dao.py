
from sqlalchemy import select

from app.Users.models import UsersModel
from app.dao.base import BaseDao
from app.database import async_session_maker
from app.exceptions import DepositConflict, UserNotRegister


class UsersDao(BaseDao):
    model = UsersModel




    @classmethod
    async def add_money(cls, user_id:int, deposit:int):
        commission = 0.05
        amount_to_add = deposit * (1 - commission)

        async  with async_session_maker() as session:
            async  with session.begin():

                query =  select(UsersModel).filter_by(id=user_id)
                result = await  session.execute(query)
                user = result.scalar_one_or_none()


                if not  user:
                    raise  UserNotRegister

                if deposit <= 0:
                    raise DepositConflict


                user.balance += amount_to_add

                return f"Ваш баланс:{user.balance}"



