from sqlalchemy import Column, ForeignKey, Integer, String
from app.core.BaseEntity import BaseEntity
from app.core.QueryEntity import QueryEntity


class CustomerEntity(BaseEntity, QueryEntity):

    __tablename__ = "Customers"

    name = Column(String(256), nullable=False, unique=True)
    avatar = Column(String(1024), nullable=False, unique=False)

    def __init__(self):
        super().__init__()

    def create(self, name, avatar=None):
        self.name = name
        self.avatar = avatar or "https://cdn.iconscout.com/icon/free/png-256/avatar-375-456327.png"
        self._validate()

    def _read_fields(self):
        return CustomerEntity.id.name

