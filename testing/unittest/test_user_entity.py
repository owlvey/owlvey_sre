import unittest

from app.core.UserEntity import UserEntity


class TestUserEntity(unittest.TestCase):

    def setUp(self):
        pass

    def test_maintenance(self):
        user = UserEntity()
        user.from_dict({"id": 123, "email": "test@hotmail.com"}, force=True)
        self.assertEqual(user.email, "test@hotmail.com")
        self.assertEqual(user.id, 123)

    def test_validate_avatar(self):
        user = UserEntity()
        user.create("email@test")

    def test_validate_email_none(self):
        user = UserEntity()
        self.assertRaises(ValueError, lambda: user.create(None, avatar=""))

    def test_to_dict(self):
        user = UserEntity()
        user.from_dict({"id": 123, "email": "test@hotmail.com"}, force=True)
        result = user.to_dict()
        self.assertTrue(result)
        self.assertTrue("email" in result)

    def test_to_hidden(self):
        user = UserEntity()
        user.from_dict({"id": 123, "email": "test@hotmail.com"}, force=True)
        user._hidden_fields = ["email"]
        result = user.to_dict()
        self.assertTrue(result)
        self.assertFalse("email" in result)








