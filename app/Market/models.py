from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, DATETIME, DateTime
from sqlalchemy.orm import relationship

from app.database import Base






class MarketModel(Base):
    __tablename__ = "Market"

    id = Column(Integer, primary_key=True)
    inventory_id = Column(ForeignKey("UserInventory.id"), nullable=False)
    seller_id = Column(ForeignKey("users.id"), nullable=False)
    price = Column(Integer, nullable=False)
    created_at = Column(DateTime,default=datetime.utcnow)


    item = relationship("UserInventoryModel", back_populates="market_lots")
    seller = relationship("UsersModel", back_populates="sales")
    def __str__(self):
        return f"{self.price} ({self.created_at})"