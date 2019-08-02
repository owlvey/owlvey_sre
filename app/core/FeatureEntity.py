from sqlalchemy import Column, ForeignKey, Integer, String
from app.core.BaseEntity import BaseEntity
from app.core.QueryEntity import QueryEntity


class FeatureEntity(BaseEntity, QueryEntity):

    __tablename__ = "Features"

    name = Column(String(256), nullable=False, unique=False)
    product_id = Column(Integer, ForeignKey('Products.id'))

    def __init__(self, name=None):
        super().__init__()
        self.name = name

    def _read_fields(self):
        return FeatureEntity.id.name

