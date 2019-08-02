from app.components.BaseComponent import BaseComponent
from app.core.BaseEntity import BaseEntity
from app.core.FeatureEntity import FeatureEntity
from app.core.ServiceEntity import ServiceEntity
from app.core.ServiceFeatureEntity import ServiceFeatureEntity


class ServicesComponent(BaseComponent):

    def __init__(self):
        super().__init__()

    def _build_entity(self) -> BaseEntity:
        return ServiceEntity()

    def register_feature(self, service_id, feature_id):
        entity = ServiceFeatureEntity()
        entity.create(service_id, feature_id)
        self._repository.create(entity)



