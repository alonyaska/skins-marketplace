import asyncio

from fastapi import APIRouter, Query
from fastapi_cache.decorator import cache

from app.skins.service import SkinsService
from app.skins.sсhemas import SSkins

router  = APIRouter(
    prefix="/AllSkins",
    tags=["Скины"],

)


@router.get("", response_model=list[SSkins])
@cache(expire=60)
async def get_all_skins(
        limit:int = Query(10, ge=1, le=100),
        offset:int = Query(0, ge=0)
):
    await  asyncio.sleep(3)
    return  await SkinsService.get_all_skins(
        limit=limit,
        offset=offset
    )


@router.get("/filter")
@cache(expire=60)
async  def get_skin_by_filter(
    user_id:int =  None,
    name: str = None,
    rarity: str = None,
    type_weapon:str = None,
    min_price: int = None,
    max_price: int = None
):
    return  await SkinsService.get_all_skins_by_filter(user_id,name, rarity,type_weapon ,min_price, max_price)


@router.get("/{id}")
async  def get_skin_by_id(id:int):
    return  await  SkinsService.get_by_id_or_404(id)