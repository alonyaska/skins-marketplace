from fastapi import  APIRouter
from fastapi.params import Depends

from app.UserInventory.schemas import SUserInventory
from app.UserInventory.service import InventoryService
from app.Users.dependencies import get_current_user


router =  APIRouter(
        prefix="/UserInventory",
        tags=["Инвентарь"],

    )


@router.get("") #response_model=list[SUserInventory])
async  def get_inventory(user: SUserInventory = Depends(get_current_user)) -> list[SUserInventory] :
     return  await InventoryService.find_all_or_404(user_id = user.id)


@router.get("/{id}")
async def get_inventory_by_id(id:int):
    return  await  InventoryService.get_by_id_or_404(id)





