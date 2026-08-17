from typing import TypeVar, Generic, Type, Optional, List
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.connector.PostgresDBConnector import session_scope

EntityType = TypeVar('EntityType')
ModelType = TypeVar('ModelType', bound=BaseModel)

class AbstractStorage(Generic[ModelType, EntityType]):
    """Базовый класс для хранилищ."""
    
    def __init__(self, entity_class: Type[EntityType], model_class: Type[ModelType]):
        self.entity_class = entity_class
        self.model_class = model_class
    
    @session_scope
    def add(self, model: ModelType, session: Session) -> int:
        """Добавить запись."""
        entity = self._model_to_entity(model)
        session.add(entity)
        session.flush()
        model.id = entity.id
        return entity.id
    
    @session_scope
    def get_by_id(self, entity_id: int, session: Session) -> Optional[ModelType]:
        """Получить по ID."""
        entity = session.query(self.entity_class).filter_by(id=entity_id).first()
        return self._entity_to_model(entity) if entity else None
    
    @session_scope
    def get_all(self, session: Session) -> List[ModelType]:
        """Получить все записи."""
        entities = session.query(self.entity_class).all()
        return [self._entity_to_model(e) for e in entities]
    
    @session_scope
    def update(self, model: ModelType, session: Session) -> Optional[ModelType]:
        """Обновить запись."""
        entity = session.query(self.entity_class).filter_by(id=model.id).first()
        if entity:
            self._update_entity(entity, model)
            return self._entity_to_model(entity)
        return None
    
    @session_scope
    def delete(self, entity_id: int, session: Session) -> bool:
        """Удалить запись."""
        entity = session.query(self.entity_class).filter_by(id=entity_id).first()
        if entity:
            session.delete(entity)
            return True
        return False
    
    # Методы для переопределения в наследниках:
    def _model_to_entity(self, model: ModelType) -> EntityType:
        """Конвертировать модель в сущность."""
        raise NotImplementedError
    
    def _entity_to_model(self, entity: EntityType) -> ModelType:
        """Конвертировать сущность в модель."""
        raise NotImplementedError
    
    def _update_entity(self, entity: EntityType, model: ModelType):
        """Обновить сущность из модели."""
        raise NotImplementedError

# Использование:
class UserStorage(AbstractStorage[UserModel, UserEntity]):
    def __init__(self):
        super().__init__(UserEntity, UserModel)
    
    def _model_to_entity(self, model: UserModel) -> UserEntity:
        return UserEntity(
            id=model.id,
            name=model.name,
            email=model.email
        )
    
    def _entity_to_model(self, entity: UserEntity) -> UserModel:
        return UserModel(
            id=entity.id,
            name=entity.name,
            email=entity.email
        )
    
    def _update_entity(self, entity: UserEntity, model: UserModel):
        entity.name = model.name
        entity.email = model.email
    
    