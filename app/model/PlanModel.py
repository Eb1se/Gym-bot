from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, ConfigDict


# 1. Основная модель
class PlanModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    user_id: int
    txt: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None


# 2. Модель создания
class PlanCreationModel(BaseModel):
    user_id: int
    txt: Optional[str] = None


# 3. Параметры редактирования
class PlanEditionParamsModel(BaseModel):
    id: int
    txt: Optional[str] = None


# 4. Модель обновления в БД
class PlanEditionModel(PlanEditionParamsModel):
    updated_at: datetime


# 5. Список
class PlanListModel(BaseModel):
    data: Optional[List[PlanModel]] = None