import unittest

from app.core.UserEntity import UserEntity


class TestUserEntity(unittest.TestCase):

    def setUp(self):
        pass

    def test_maintenance(self):
        user = UserEntity()
        user.from_dict({"user_id": "123", "email": "test@hotmail.com"})
        print(user.to_dict())

    def test_validate_avatar(self):
        user = UserEntity()
        user.create("email@test")

    def test_validate_email_none(self):
        user = UserEntity()
        self.failUnlessRaises(ValueError, lambda: user.create(None, avatar=""))







