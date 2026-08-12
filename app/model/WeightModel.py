from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, ConfigDict


# 1. Основная модель
class WeightModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    user_id: int
    weight: float
    date: datetime
    updated_at: Optional[datetime] = None


# 2. Модель создания
class WeightCreationModel(BaseModel):
    user_id: int
    weight: float
    date: Optional[datetime] = None


# 3. Параметры редактирования
class WeightEditionParamsModel(BaseModel):
    id: int
    weight: Optional[float] = None


# 4. Модель обновления в БД
class WeightEditionModel(WeightEditionParamsModel):
    updated_at: datetime


# 5. Список
class WeightListModel(BaseModel):
    data: Optional[List[WeightModel]] = None
