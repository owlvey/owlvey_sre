from sqlalchemy import Column, ForeignKey, Integer, String
from app.core.BaseEntity import BaseEntity
from app.core.QueryEntity import QueryEntity


class ProductEntity(BaseEntity, QueryEntity):

    __tablename__ = "Products"

    name = Column(String(256), nullable=False, unique=False)
    customer_id = Column(Integer, ForeignKey('Customers.id'))

    def __init__(self):
        super().__init__()

    def _read_fields(self):
        return ProductEntity.id.name

