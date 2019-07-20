from app.components.BaseComponent import BaseComponent
from app.core.BaseEntity import BaseEntity
from app.core.ProductEntity import ProductEntity


class ProductsComponent(BaseComponent):

    def __init__(self):
        super().__init__()

    def _build_entity(self) -> BaseEntity:
        return ProductEntity()
