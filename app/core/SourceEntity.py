from sqlalchemy import Column, ForeignKey, Integer, String
from app.core.BaseEntity import BaseEntity
from app.core.QueryEntity import QueryEntity


class SourceEntity(BaseEntity, QueryEntity):

    __tablename__ = "Sources"

    name = Column(String(256), nullable=False, unique=True)

    def __init__(self, name=None):
        super().__init__()
        self.name = name

    def _read_fields(self):
        return SourceEntity.id.name

