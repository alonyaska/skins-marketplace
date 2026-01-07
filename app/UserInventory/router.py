from fastapi import  APIRouter


from app.UserInventory.schemas import SUserInventory
from app.UserInventory.service import InventoryService

router =  APIRouter(
        prefix="/UserInventory",
        tags=["Инвентарь"],

    )


@router.get("", response_model=list[SUserInventory])
async  def get_inventory() :
    return  await InventoryService.get_inventory_or_404()


@router.get("/{id}")
async def get_inventory_by_id(id:int):
    return  await  InventoryService.get_by_id_or_404(id)





