from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from app.core.BaseEntity import BaseEntity
from app.core.QueryEntity import QueryEntity


class JournalEntity(BaseEntity, QueryEntity):

    __tablename__ = "Journals"

    source_id = Column(Integer, ForeignKey('Sources.id'))
    good = Column(Integer, nullable=False)
    total = Column(Integer, nullable=False)
    start = Column(DateTime, nullable=False)
    end = Column(DateTime, nullable=False)

    def __init__(self, name=None):
        super().__init__()
        self.name = name

    def _read_fields(self):
        return JournalEntity.id.name

