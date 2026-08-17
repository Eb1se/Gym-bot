from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.entity.BaseEntity import BaseEntity
from app.utils.date_time_utils import utc_now

class PlanEntity(BaseEntity):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    txt = Column(String, nullable=True)
    
    created_at = Column(DateTime, default=utc_now, nullable=False)
    updated_at = Column(DateTime, default=utc_now, onupdate=utc_now)

    user = relationship("UserEntity", back_populates="plans")
