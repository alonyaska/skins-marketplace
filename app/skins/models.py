

from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship

from  app.database import Base



class SkinsModel(Base):
    __tablename__ = "skins"


    id = Column(Integer, primary_key=True)
    owner_id = Column(ForeignKey("users.id"))
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    date = Column(Integer, nullable=False)
    asset = Column(JSON)
    rarity = Column(String, nullable=False)
    image_id = Column(Integer)

    inventory_entries = relationship("UserInventoryModel", back_populates="skin")

