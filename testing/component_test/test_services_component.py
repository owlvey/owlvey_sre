import unittest

from app.components.CustomersComponent import CustomersComponent
from app.components.FeaturesComponent import FeaturesComponent
from app.components.ProductsComponent import ProductsComponent
from app.components.ServicesComponent import ServicesComponent
from testing.DataSeed import DataSeed
from testing.component_test.ComponentDataSeed import ComponentDataSeed


class TestServiceComponent(unittest.TestCase):

    def setUp(self):
        self.customer_component = CustomersComponent()
        self.product_component = ProductsComponent()
        self.service_component = ServicesComponent()
        self.feature_component = FeaturesComponent()

    def test_maintenance(self):
        name = DataSeed.generate_name("service_{}")
        product = ComponentDataSeed.build_product(self.customer_component, self.product_component)
        self.service_component.create({"name": name, "product_id": product["id"]})

    def test_feature_registration(self):
        product = ComponentDataSeed.build_product(self.customer_component, self.product_component)
        service = ComponentDataSeed.build_service(product, self.service_component)
        feature = ComponentDataSeed.build_feature(product, self.feature_component)
        self.service_component.register_feature(service["id"], feature["id"])























