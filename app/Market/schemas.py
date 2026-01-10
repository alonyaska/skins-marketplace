from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.UserInventory.schemas import SUserInventory
from app.Users.schemas import SUsers


class SMarket(BaseModel):
    id: int
    inventory_id: int
    seller_id: int
    price: int
    created_at: datetime

    item: SUserInventory | None = None
    seller: SUsers| None = None

    model_config = ConfigDict(from_attributes=True)