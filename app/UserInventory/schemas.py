from pydantic import BaseModel, ConfigDict

from app.skins.shemas import SSkins


class SUserInventory(BaseModel):
    id: int
    user_id: int
    skin_id: int
    float_value: float
    is_on_sale: bool | None = None
    is_on_discount: int | None = None

    skin:SSkins |None = None

    model_config = ConfigDict(from_attributes=True)