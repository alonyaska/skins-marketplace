from sqladmin import ModelView

from app.Market.models import MarketModel
from app.UserInventory.models import UserInventoryModel
from app.Users.models import UsersModel
from app.skins.models import SkinsModel


class UserAdmin(ModelView, model=UsersModel):
    column_list = [UsersModel.id,UsersModel.email ,UsersModel.username, UsersModel.balance]
    can_delete = False
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"


class UserInventAdmin(ModelView, model=UserInventoryModel):

    column_list = [
        UserInventoryModel.id,
        UserInventoryModel.user_id,
        UserInventoryModel.skin,
        UserInventoryModel.float_value,
        UserInventoryModel.is_on_sale
    ]


    column_filters = []


    column_searchable_list = [UserInventoryModel.user_id]

    can_delete = False
    name = "Инвентарь"
    name_plural = "Инвентари"
    icon = "fa-solid fa-box-open"



class SkinsModelAdmin(ModelView, model=SkinsModel):

    column_list = [
        SkinsModel.id,
        SkinsModel.name,
        SkinsModel.rarity,
        SkinsModel.type_weapon,
        SkinsModel.asset
    ]

    can_delete = False
    name = "Скин"
    name_plural = "Библиотека Скинов"
    icon = "fa-solid fa-book"



class MarketModelAdmin(ModelView, model=MarketModel):

    column_list = [
        MarketModel.inventory_id,
        MarketModel.seller_id,
        MarketModel.price,
        MarketModel.created_at
    ]


    can_delete =  True
    name = "Лот"
    name_plural = "Маркет"
    icon = "fa-solid fa-shop"

