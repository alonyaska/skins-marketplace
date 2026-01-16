from fastapi import  APIRouter
from fastapi.params import Depends, Query
from fastapi_cache.decorator import cache

from app.UserInventory.schemas import SUserInventory
from app.UserInventory.service import InventoryService
from app.Users.dependencies import get_current_user
from app.skins.sсhemas import SSkins

router =  APIRouter(
        prefix="/UserInventory",
        tags=["Инвентарь"],

    )


@router.get("")
@cache(expire=60)#response_model=list[SUserInventory])
async  def get_inventory(user: SUserInventory = Depends(get_current_user)) -> list[SUserInventory] :
     return  await InventoryService.get_inventory_or_404(user_id = user.id)


@router.get("/filter")
@cache(expire=60)
async def get_filter_inventory(
        user: SUserInventory = Depends(get_current_user),
        name: str | None = Query(None, description="Поиск по названию скина"),
        rarity: str | None = Query(None, description="Фильтр по редкости (Base, Covert и т.д.)"),
        type_weapon: str | None = Query(None, description="Тип оружия (Knife, Rifle)"),
) -> list[SSkins]:
    return  await InventoryService.filtered_inventory(
        user_id = user.id,
        name=name,
        rarity=rarity,
        type_weapon=type_weapon,
        )


@router.get("/{id}")
@cache(expire=60)
async def get_inventory_by_id(id:int):
    return  await  InventoryService.get_by_id_or_404(id)





