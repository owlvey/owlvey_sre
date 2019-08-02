from threading import Thread

from sqlalchemy import Column, ForeignKey, Integer, String
from app.core.BaseEntity import BaseEntity
from app.core.QueryEntity import QueryEntity


class ServiceFeatureEntity(BaseEntity, QueryEntity):
    __tablename__ = "ServiceFeatures"

    service_id = Column(Integer, ForeignKey('Services.id'))
    feature_id = Column(Integer, ForeignKey('Features.id'))

    def __init__(self):
        super().__init__()

    def create(self, service_id, feature_id):
        self.service_id = service_id
        self.feature_id = feature_id
        self._validate()

    def _read_fields(self):
        return ServiceFeatureEntity.id.name

