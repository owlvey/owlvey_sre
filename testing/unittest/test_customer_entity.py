import unittest

from app.core.CustomerEntity import CustomerEntity
from app.core.UserEntity import UserEntity


class TestCustomerEntity(unittest.TestCase):

    def setUp(self):
        pass

    def test_maintenance(self):
        entity = CustomerEntity()
        entity.from_dict({"id": 123, "name": "test@hotmail.com"}, force=True)
        self.assertEqual(entity.name, "test@hotmail.com")
        self.assertEqual(entity.id, 123)

    def test_from_dict_detect(self):
        entity = CustomerEntity()
        self.assertRaises(ValueError,
                          lambda: entity.from_dict({"id": 123, "email": "test@hotmail.com"}, force=True))

    def test_validate_avatar(self):
        entity = CustomerEntity()
        entity.create("email@test")

    def test_validate_name_none(self):
        entity = CustomerEntity()
        self.assertRaises(ValueError,
                          lambda: entity.create(None, avatar=""))







