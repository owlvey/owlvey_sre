from app.core.EntityUtils import EntityUtils
from app.core.CustomerEntity import CustomerEntity
from app.repositories.EntityRepository import EntityRepository


class CustomersComponent:

    def __init__(self):
        self.repository = EntityRepository()

    def create(self, data):
        user = CustomerEntity()
        user.from_dict(data)
        self.repository.create(user)

    def list(self):
        customers = CustomerEntity.query.all()
        return EntityUtils.entities_to_list_dictionaries(customers)

    def get(self, key):
        customer = CustomerEntity.query.filter(CustomerEntity.user_id == key).first()
        return customer.to_dict() if customer else None

    def delete(self, key):
        user = CustomerEntity.query.filter(CustomerEntity.user_id == key).first()
        self.repository.delete(user)

    def update(self, data):
        user = CustomerEntity.query.filter(CustomerEntity.user_id == data[CustomerEntity.customer_id.name]).first()
        user.from_dict(data)
        self.repository.update(user)
