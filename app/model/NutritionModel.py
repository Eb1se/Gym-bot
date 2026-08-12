from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, ConfigDict


# 1. Основная модель
class NutritionModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    user_id: int
    calories: int
    proteins: int
    fat: int
    carbs: int
    file_id: Optional[str] = None
    file_type: Optional[str] = None
    date: datetime
    updated_at: Optional[datetime] = None


# 2. Модель создания

class NutritionCreationModel(BaseModel):
    user_id: int
    calories: Optional[int] = 0
    proteins: Optional[int] = 0
    fat: Optional[int] = 0
    carbs: Optional[int] = 0
    file_id: Optional[str] = None
    file_type: Optional[str] = None
    date: Optional[datetime] = None


# 3. Параметры редактирования
class NutritionEditionParamsModel(BaseModel):
    id: int
    calories: Optional[int] = None
    proteins: Optional[int] = None
    fat: Optional[int] = None
    carbs: Optional[int] = None


# 4. Модель обновления в БД
class NutritionEditionModel(NutritionEditionParamsModel):
    updated_at: datetime


# 5. Список
class NutritionListModel(BaseModel):
    data: Optional[List[NutritionModel]] = None
