from app.components.BaseComponent import BaseComponent
from app.core.BaseEntity import BaseEntity
from app.core.ProductEntity import ProductEntity


class ProductsComponent(BaseComponent):

    def __init__(self):
        super().__init__()

    def _build_entity(self) -> BaseEntity:
        return ProductEntity()

    def get_by_customer_id_name(self, customer_id, name):
        entity = ProductEntity.query.filter(ProductEntity.customer_id == customer_id
                                            and ProductEntity.name == name).first()
        return entity.to_dict()
