from sqlalchemy import Column, ForeignKey, Integer, String
from app.core.BaseEntity import BaseEntity
from app.core.QueryEntity import QueryEntity


class CustomerEntity(BaseEntity, QueryEntity):

    __tablename__ = "Customers"

    name = Column(String(256), nullable=False, unique=True)

    def __init__(self):
        super().__init__()

    def _read_fields(self):
        return CustomerEntity.id.name

