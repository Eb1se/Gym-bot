from datetime import datetime
from typing import Optional, Dict, Any, List
from pydantic import BaseModel, ConfigDict


# 1. Основная модель пользователей
class UserModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    telegram_id: int
    username: Optional[str] = None
    first_name: Optional[str] = None
    timezone_offset: int = 3
    created_at: datetime
    last_activity: datetime
    is_active: bool = True
    settings: Optional[Dict[str, Any]] = None


# 2. Модель для регистрации / создания пользователя
class UserCreationModel(BaseModel):
    telegram_id: int
    username: Optional[str] = None
    first_name: Optional[str] = None
    timezone_offset: Optional[int] = 3
    settings: Optional[Dict[str, Any]] = None


# 3. Параметры для редактирования профиля/настроек
class UserEditionParamsModel(BaseModel):
    id: int
    username: Optional[str] = None
    first_name: Optional[str] = None
    timezone_offset: Optional[int] = None
    is_active: Optional[bool] = None
    settings: Optional[Dict[str, Any]] = None


# 4. Модель обновления в БД (обновляет также активность)
class UserEditionModel(UserEditionParamsModel):
    last_activity: datetime


# 5. Список пользователей
class UserListModel(BaseModel):
    data: Optional[List[UserModel]] = None
    total: Optional[int] = None
