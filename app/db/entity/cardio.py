from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.entity.BaseEntity import BaseEntity
from app.utils.date_time_utils import utc_now


class CardioEntity(BaseEntity):
    __tablename__ = "cardio"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    type = Column(String, nullable=False)
    time = Column(Float, nullable=False)
    pulse = Column(String, nullable=True)
    lost_calories = Column(Integer, nullable=True)
    
    datetime = Column(DateTime, default=utc_now, nullable=False)
    updated_at = Column(DateTime, default=utc_now, onupdate=utc_now)

    user = relationship("UserEntity", back_populates="cardio")
