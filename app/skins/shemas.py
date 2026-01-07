from pydantic import BaseModel, ConfigDict
from typing import Any


class SSkins(BaseModel):

    id:int
    name:str
    price:int
    date:int
    asset: dict[str, Any] | None = None
    rarity: str
    image_id: int



    model_config = ConfigDict(from_attributes=True)
