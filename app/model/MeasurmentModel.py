from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, ConfigDict


# 1. Основная модель
class MeasurementsModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    user_id: int
    chest: Optional[float] = None
    waistline: Optional[float] = None
    stomach: Optional[float] = None
    hips: Optional[float] = None
    biceps: Optional[float] = None
    shoulders: Optional[float] = None
    height: Optional[int] = None
    date: datetime
    updated_at: Optional[datetime] = None


# 2. Модель создания
class MeasurementsCreationModel(BaseModel):
    user_id: int
    chest: Optional[float] = None
    waistline: Optional[float] = None
    stomach: Optional[float] = None
    hips: Optional[float] = None
    biceps: Optional[float] = None
    shoulders: Optional[float] = None
    height: Optional[int] = None


# 3. Параметры редактирования
class MeasurementsEditionParamsModel(BaseModel):
    id: int
    chest: Optional[float] = None
    waistline: Optional[float] = None
    stomach: Optional[float] = None
    hips: Optional[float] = None
    biceps: Optional[float] = NoneА
    shoulders: Optional[float] = None
    height: Optional[int] = None


# 4. Модель для обновления в БД
class MeasurementsEditionModel(MeasurementsEditionParamsModel):
    updated_at: datetime


# 5. Список
class MeasurementsListModel(BaseModel):
    data: Optional[List[MeasurementsModel]] = None