import unittest
import itertools
import os
from app.components.CustomersComponent import CustomersComponent
from app.components.FeaturesComponent import FeaturesComponent
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

        items = list(itertools.product(customers, products))

        for item in list(items):
            tmp_customer = customer_component.get_by_name(item[0])
            product_component.create({"name": item[1], "customer_id": tmp_customer["id"]})

        services = ["registration", "payments", "loans", "campaigns"]

        service_component = ServicesComponent()
        feature_component = FeaturesComponent()

        features = ["otp", "login", "search account", "make payment", "rapid cash"]

        for item in items:
            tmp_customer = customer_component.get_by_name(item[0])
            tmp_product = product_component.get_by_customer_id_name(tmp_customer["id"], item[1])
            for service in services:
                service_component.create({"name": service, "product_id": tmp_product["id"]})

            for feature in features:
                feature_component.create({"name": feature, "product_id": tmp_product["id"]})

        registration_service = service_component.get_by_name("registration")
        payment_service = service_component.get_by_name("payments")
        campaigns_service = service_component.get_by_name("campaigns")

        otp_feature = feature_component.get_by_name("otp")
        login_feature = feature_component.get_by_name("login")
        search_feature = feature_component.get_by_name("search account")
        make_payment_feature = feature_component.get_by_name("make payment")
        rapid_cash_feature = feature_component.get_by_name("rapid cash")

        service_component.register_feature(registration_service["id"], otp_feature["id"])
        service_component.register_feature(registration_service["id"], login_feature["id"])
        service_component.register_feature(payment_service["id"], otp_feature["id"])
        service_component.register_feature(payment_service["id"], login_feature["id"])
        service_component.register_feature(payment_service["id"], search_feature["id"])
        service_component.register_feature(payment_service["id"], make_payment_feature["id"])

        service_component.register_feature(campaigns_service["id"], otp_feature["id"])
        service_component.register_feature(campaigns_service["id"], login_feature["id"])
        service_component.register_feature(campaigns_service["id"], search_feature["id"])
        service_component.register_feature(campaigns_service["id"], rapid_cash_feature["id"])




























