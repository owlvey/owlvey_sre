from app.components.BaseComponent import BaseComponent
from app.core.BaseEntity import BaseEntity
from app.core.FeatureEntity import FeatureEntity


class FeaturesComponent(BaseComponent):

    def __init__(self):
        super().__init__()

    def _build_entity(self) -> BaseEntity:
        return FeatureEntity()
