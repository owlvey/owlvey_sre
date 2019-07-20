from app.core.BaseEntity import BaseEntity
from app.core.EntityUtils import EntityUtils
from app.repositories.EntityRepository import EntityRepository
from abc import abstractmethod


class BaseComponent:

    def __init__(self):
        self._repository = EntityRepository()

    @abstractmethod
    def _build_entity(self) -> BaseEntity:
        pass

    def create(self, data):
        entity = self._build_entity()
        entity.from_dict(data)
        self._repository.create(entity)

    def list(self):
        entity = self._build_entity()
        items = entity.query.all()
        return EntityUtils.entities_to_list_dictionaries(items)

    def get(self, key):
        entity = self._build_entity()
        cls = type(entity)
        item = cls.query.filter(cls.id == key).first()
        return item.to_dict() if item else None

    def delete(self, key):
        entity = self._build_entity()
        cls = type(entity)
        item = cls.query.filter(cls.id == key).first()
        self._repository.delete(item)

    def update(self, data):
        entity = self._build_entity()
        cls = type(entity)
        item = cls.query.filter(cls.id == data[cls.id.name]).first()
        item.from_dict(data)
        self._repository.update(item)
        return item.to_dict()
