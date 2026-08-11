from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.utils.date_time_utils import utc_now

class MeasurementsEntity(Base):
    __tablename__ = "measurements"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    chest = Column(Float, nullable=True)
    waistline = Column(Float, nullable=True)
    stomach = Column(Float, nullable=True)
    hips = Column(Float, nullable=True)
    biceps = Column(Float, nullable=True)
    shoulders = Column(Float, nullable=True)
    height = Column(Integer, nullable=True)
    
    date = Column(DateTime, default=utc_now, nullable=False)
    updated_at = Column(DateTime, default=utc_now, onupdate=utc_now)
    
    user = relationship("UserEntity", back_populates="measurements")