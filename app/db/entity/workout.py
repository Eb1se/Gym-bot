from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.entity.BaseEntity import BaseEntity
from app.utils.date_time_utils import utc_now


class WorkoutEntity(BaseEntity):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    datetime = Column(DateTime, default=utc_now)
    notes = Column(Text, nullable=True)
    training_time = Column(Float, nullable=False)
    quality = Column(Integer, nullable=True)

    user = relationship("UserEntity", back_populates="workouts")
    sets = relationship("SetEntity", back_populates="workout", cascade="all, delete-orphan")


class SetEntity(BaseEntity):
    __tablename__ = "sets"

    id = Column(Integer, primary_key=True)
    workout_id = Column(Integer, ForeignKey("workouts.id", ondelete="CASCADE"), nullable=False)
    exercise = Column(String, nullable=False)
    set_number = Column(Integer, nullable=False)
    weight = Column(Float, nullable=False)
    reps = Column(Integer, nullable=False)
    rest_time = Column(Integer, nullable=False)
    notes = Column(String, nullable=True)

    workout = relationship("WorkoutEntity", back_populates="sets")
