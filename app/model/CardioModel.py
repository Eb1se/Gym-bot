from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, ConfigDict


# 1. Основная модель
class CardioModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    user_id: int
    type: str
    time: float
    pulse: Optional[str] = None
    lost_calories: Optional[int] = None
    datetime: datetime
    updated_at: Optional[datetime] = None


# 2. Модель для создания
class CardioCreationModel(BaseModel):
    user_id: int
    type: str
    time: float
    pulse: Optional[str] = None
    lost_calories: Optional[int] = None
    datetime: Optional[datetime] = None


# 3. Параметры для редактирования
class CardioEditionParamsModel(BaseModel):
    id: int
    type: Optional[str] = None
    time: Optional[float] = None
    pulse: Optional[str] = None
    lost_calories: Optional[int] = None


# 4. Модель обновления в БД
class CardioEditionModel(CardioEditionParamsModel):
    updated_at: datetime


# 5. Список
class CardioListModel(BaseModel):
    data: Optional[List[CardioModel]] = None
