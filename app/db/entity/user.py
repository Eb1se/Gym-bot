from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Boolean, JSON
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.utils.date_time_utils import utc_now


class UserEntity(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(BigInteger(), unique=True, nullable=False)
    username = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    created_at = Column(DateTime, default=utc_now)
    last_activity = Column(DateTime, default=utc_now)
    is_active = Column(Boolean, default=True)
    settings = Column(JSON, default={
        "features": {
            "workout": True,      # тренировки
            "nutrition": True,    # КБЖУ
            "measurements": True,  # замеры
            "cardio": True,       # кардио
            "weight": True,       # взвешивание
            "streak": True,       # Стрик
            "sleep": True,        # Сон
            "training_plan": True  # План тренировок
        },
    },
    )

    workouts = relationship("WorkoutEntity", back_populates="user", cascade="all, delete-orphan")
    nutritions = relationship("NutritionEntity", back_populates="user", cascade="all, delete-orphan")
    cardio = relationship("CardioEntity", back_populates="user", cascade="all, delete-orphan")
    measurements = relationship("MeasurementsEntity", back_populates="user", cascade="all, delete-orphan")
    weight = relationship("WeightEntity", back_populates="user", cascade="all, delete-orphan")
    sleep = relationship("SleepEntity", back_populates="user", cascade="all, delete-orphan")
    plans = relationship("PlanEntity", back_populates="user", cascade="all, delete-orphan")

