from fastapi import APIRouter


from app.skins.dao import SkinsDao
from app.skins.service import SkinsService
from app.skins.shemas import SSkins

router  = APIRouter(
    prefix="/AllSkins",
    tags=["Скины"],

)


@router.get("", response_model=list[SSkins])
async def get_all_skins():
    return  await SkinsService.get_all_skins()



@router.get("/{id}")
async  def get_skin_by_id(id:int):
    return  await  SkinsService.get_by_id_or_404(id)