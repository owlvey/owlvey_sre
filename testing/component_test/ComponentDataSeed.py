from app.components.CustomersComponent import CustomersComponent
from app.components.FeaturesComponent import FeaturesComponent
from app.components.ProductsComponent import ProductsComponent
from app.components.ServicesComponent import ServicesComponent
from testing.DataSeed import DataSeed


class ComponentDataSeed:

    def __init__(self):
        pass

    @staticmethod
    def build_customer(customer_component: CustomersComponent):
        name = DataSeed.generate_name("customer_{}")
        customer_component.create({"name": name})
        customer = customer_component.get_by_name(name)
        return customer

    @staticmethod
    def build_product(customer_component: CustomersComponent,
                      product_component: ProductsComponent):

        name = DataSeed.generate_name("product_{}")
        customer = ComponentDataSeed.build_customer(customer_component)
        product_component.create({"name": name, "customer_id": customer["id"]})
        product = product_component.get_by_name(name)
        return product

    @staticmethod
    def build_service(product, service_component: ServicesComponent):
        name = DataSeed.generate_name("service_{}")
        service_component.create({"name": name, "product_id": product["id"]})
        return service_component.get_by_name_relation_id(product["id"], name)

    @staticmethod
    def build_feature(product, feature_component: FeaturesComponent):
        name = DataSeed.generate_name("feature_{}")
        feature_component.create({"name": name, "product_id": product["id"]})
        return feature_component.get_by_name(name)


