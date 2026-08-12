from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, ConfigDict


# 1. Основная модель
class SleepModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    user_id: int
    sleep_start: Optional[datetime] = None
    sleep_end: Optional[datetime] = None
    time_sleep: float
    quality: int
    created_at: datetime
    updated_at: Optional[datetime] = None


# 2. Модель для создания
class SleepCreationModel(BaseModel):
    user_id: int
    time_sleep: float
    quality: int
    sleep_start: Optional[datetime] = None
    sleep_end: Optional[datetime] = None


# 3. Параметры для редактирования
class SleepEditionParamsModel(BaseModel):
    id: int
    time_sleep: Optional[float] = None
    quality: Optional[int] = None
    sleep_start: Optional[datetime] = None
    sleep_end: Optional[datetime] = None


# 4. Модель обновления в БД
class SleepEditionModel(SleepEditionParamsModel):
    updated_at: datetime


# 5. Список
class SleepListModel(BaseModel):
    data: Optional[List[SleepModel]] = None
