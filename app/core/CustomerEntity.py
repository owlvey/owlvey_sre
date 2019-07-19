from sqlalchemy import Column, ForeignKey, Integer, String
from app.core.BaseEntity import BaseEntity
from app.core.QueryEntity import QueryEntity


class CustomerEntity(BaseEntity, QueryEntity):

    __tablename__ = "Customers"

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)

    def __init__(self):
        super().__init__()

    def _read_fields(self):
        return CustomerEntity.customer_id.name

