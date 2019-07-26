import unittest

from app.components.CustomersComponent import CustomersComponent
from app.components.SubscriptionsComponent import SubscriptionsComponent
from app.components.UsersComponent import UsersComponent
from testing.DataSeed import DataSeed


class TestCustomersComponent(unittest.TestCase):

    def setUp(self):
        self.customer_component = CustomersComponent()
        self.user_component = UsersComponent()
        self.subscription_component = SubscriptionsComponent()

    def test_maintenance(self):
        email = DataSeed.generate_name("account{}@email.com")
        name = DataSeed.generate_name("name {}")
        self.customer_component.create({"name": name})
        self.user_component.create({"email": email})
        customer = self.customer_component.get_by_name(name)
        user = self.user_component.get_by_email(email)

        self.subscription_component.create({"customer_id": customer["id"], "user_id": user["id"]})

        subscription = self.subscription_component.get_by_customer_user(customer["id"], user["id"])

        self.assertTrue(subscription)
















