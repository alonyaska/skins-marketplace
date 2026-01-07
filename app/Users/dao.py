from app.Users.models import UsersModel
from app.dao.base import BaseDao


class UsersDao(BaseDao):
    model = UsersModel