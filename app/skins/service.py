
from fastapi import Query


from app.exceptions import InventoryNotFound
from app.skins.dao import SkinsDao
from app.skins.sсhemas import SSkins
from app.dao.skins_base import SkinsBaseDao


class SkinsService:


    @classmethod
    async  def get_by_id_or_404(cls, model_id:int):
        result = await  SkinsDao.find_by_id(model_id)
        if not result:
            raise  InventoryNotFound()
        return result


    @classmethod
    async def get_all_skins(
                            cls,
                            limit:int,
                            offset:int
    ):
        return  await SkinsDao.get_all_skins(
            limit=limit,
            offset=offset
        )


    @classmethod
    async  def get_all_skins_by_filter(
            cls,
            user_id: int = Query(None, description="Поиск по id"),
            name: str = Query(None, description="Поиск по названию"),
            rarity: str = Query(None, description="Фильтр по редкости"),
            type_weapon: str = Query(None, description="Фильтр по типу Оружия"),
            min_price: int = Query(None, description="Минимальная цена"),
            max_price: int = Query(None, description="Максимальная цена")
        ) -> list[SSkins]:
        return  await  SkinsDao.apply_filtres(
            user_id=user_id,
            name=name,
            rarity=rarity,
            type_weapon=type_weapon,
            min_price=min_price,
            max_price=max_price
        )