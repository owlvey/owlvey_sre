import unittest

from app.components.UsersComponent import UsersComponent
from testing.DataSeed import DataSeed


class TestUsersComponent(unittest.TestCase):

    def setUp(self):
        self.component = UsersComponent()

    def test_maintenance(self):

        email = DataSeed.generate_name("account{}@email.com")

        self.component.create({"email": email})

        users = self.component.list()

        self.assertTrue(users)

        user = self.component.get(users[0]["user_id"])

        user["email"] = "change"

        self.component.update(user)

        user = self.component.get(user["user_id"])

        self.assertEqual(user["email"], "change")

        self.component.delete(user["user_id"])

        user = self.component.get(user["user_id"])

        self.assertFalse(user)


