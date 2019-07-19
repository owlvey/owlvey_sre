import unittest

from app.core.UserEntity import UserEntity


class TestUserEntity(unittest.TestCase):

    def setUp(self):
        pass

    def test_maintenance(self):
        user = UserEntity()
        user.from_dict({"user_id": "123", "email": "test@hotmail.com"})
        print(user.to_dict())




