from app.components.BaseComponent import BaseComponent
from app.core.CustomerEntity import CustomerEntity


class CustomersComponent(BaseComponent):

    def __init__(self):
        super().__init__()

    def _build_entity(self) -> CustomerEntity:
        return CustomerEntity()

    def get_by_name(self, name):
        customer = CustomerEntity.query.filter(CustomerEntity.name == name).first()
        return customer.to_dict()

