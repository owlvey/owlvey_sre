import unittest
import itertools
import os
from app.components.CustomersComponent import CustomersComponent
from app.components.ProductsComponent import ProductsComponent
from app.components.ServicesComponent import ServicesComponent
from app.components.SquadsComponent import SquadsComponent
from app.components.SubscriptionsComponent import SubscriptionsComponent
from app.components.UsersComponent import UsersComponent


class TestOwlveyBasic(unittest.TestCase):

    def setUp(self):
        self.current_dir = os.getcwd()

    def build_squads(self):
        squads = ["naboo", "coruscant"]
        squad_component = SquadsComponent()
        for squad in squads:
            squad_component.create({"name": squad})

    def test_maintenance(self):

        customer_component = CustomersComponent()
        customers = ["bcp", "jpmorgan", "scotiabank"]

        for customer in customers:
            customer_component.create({"name": customer})

        users = ["gregory@email.com", "felipe@email.com", "olga984@email.com"]

        users_component = UsersComponent()
        for user in users:
            users_component.create({"email": user})

        items = itertools.product(customers, users)

        subscription_component = SubscriptionsComponent()

        for item in list(items):
            tmp_customer = customer_component.get_by_name(item[0])
            tmp_user = users_component.get_by_email(item[1])
            subscription_component.create(
                {
                    "user_id": tmp_user["id"],
                    "customer_id": tmp_customer["id"]
                }
            )

        self.build_squads()

        products = ["blue", "yellow", "red"]
        product_component = ProductsComponent()

        items = itertools.product(customers, products)

        for item in list(items):
            tmp_customer = customer_component.get_by_name(item[0])
            product_component.create({"name": item[1], "customer_id": tmp_customer["id"]})

        services = ["login", "registration", "payments", "loans"]
        services = {
            "login": ["otp"]
        }
        service_component = ServicesComponent()

        for item in list(items):
            tmp_customer = customer_component.get_by_name(item[0])
            tmp_product = product_component.get_by_customer_id_name(tmp_customer["id"], item[1])
            for service in services:
                service_component.create({"name": service, "product_id": tmp_product["id"]})

















