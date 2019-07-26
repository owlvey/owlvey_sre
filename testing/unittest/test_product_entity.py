import unittest
from app.core.ProductEntity import ProductEntity


class TestCustomerEntity(unittest.TestCase):

    def setUp(self):
        pass

    def test_maintenance(self):
        entity = ProductEntity()
        entity.create(name="test@hotmail.com")
        self.assertEqual(entity.name, "test@hotmail.com")

