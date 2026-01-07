from sqlalchemy import Column, Integer, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship

from  app.database import Base



class UserInventoryModel(Base):
    __tablename__ = "UserInventory"


    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.id"))
    skin_id = Column(ForeignKey("skins.id"))
    float_value = Column(Float, nullable=False)
    is_on_sale = Column(Boolean, default=False)
    is_on_discount = Column(Integer, nullable=True)



    skin = relationship("SkinsModel", back_populates="inventory_entries")
    user = relationship("UsersModel", back_populates="inventory")
