from app.components.BaseComponent import BaseComponent
from app.core.BaseEntity import BaseEntity
from app.core.SourceEntity import SourceEntity


class SourcesComponent(BaseComponent):

    def __init__(self):
        super().__init__()

    def _build_entity(self) -> BaseEntity:
        return SourceEntity()
