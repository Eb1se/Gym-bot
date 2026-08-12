from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, ConfigDict


# 1. Основная модель (ответ из БД)
class WorkoutModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    user_id: int
    datetime: datetime
    notes: Optional[str] = None
    training_time: float
    quality: Optional[int] = None
    updated_at: Optional[datetime] = None


# 2. Модель для создания (POST /workouts)
class WorkoutCreationModel(BaseModel):
    user_id: int
    training_time: float
    datetime: Optional[datetime] = None
    notes: Optional[str] = None
    quality: Optional[int] = None


# 3. Параметры для редактирования (ввод пользователя)
class WorkoutEditionParamsModel(BaseModel):
    id: int
    notes: Optional[str] = None
    training_time: Optional[float] = None
    quality: Optional[int] = None


# 4. Модель для сохранения изменений в БД
class WorkoutEditionModel(WorkoutEditionParamsModel):
    updated_at: datetime


# 5. Модель списка
class WorkoutListModel(BaseModel):
    data: Optional[List[WorkoutModel]] = None
    total: Optional[int] = None
