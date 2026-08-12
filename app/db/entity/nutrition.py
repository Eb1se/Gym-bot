from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.utils.date_time_utils import utc_now


class NutritionEntity(Base):
    __tablename__ = "nutritions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    calories = Column(Integer, nullable=False)
    proteins = Column(Integer, nullable=False)
    fat = Column(Integer, nullable=False)
    carbs = Column(Integer, nullable=False)
    file_id = Column(String, nullable=True)
    file_type = Column(String, nullable=True)
    
    date = Column(DateTime, default=utc_now, nullable=False)
    updated_at = Column(DateTime, default=utc_now, onupdate=utc_now)
    
    user = relationship("UserEntity", back_populates="nutritions")
