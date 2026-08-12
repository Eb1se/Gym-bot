from typing import Optional, List
from pydantic import BaseModel, ConfigDict


# 1. Основная модель
class SetModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    workout_id: int
    exercise: str
    set_number: int
    weight: float
    reps: int
    rest_time: int
    notes: Optional[str] = None


# 2. Модель для создания
class SetCreationModel(BaseModel):
    workout_id: int
    exercise: str
    set_number: int
    weight: float
    reps: int
    rest_time: int
    notes: Optional[str] = None


# 3. Параметры для редактирования
class SetEditionParamsModel(BaseModel):
    id: int
    exercise: Optional[str] = None
    set_number: Optional[int] = None
    weight: Optional[float] = None
    reps: Optional[int] = None
    rest_time: Optional[int] = None
    notes: Optional[str] = None


# 4. Модель для сервисного слоя
class SetEditionModel(SetEditionParamsModel):
    pass


# 5. Список подходов
class SetListModel(BaseModel):
    data: Optional[List[SetModel]] = None
