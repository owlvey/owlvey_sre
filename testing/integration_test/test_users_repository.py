import unittest
from app.components.ConfigurationComponent import ConfigurationComponent
from app.core.UserEntity import UserEntity
from app.core.UsersFrame import UsersFrame
from app.repositories.UsersRepository import UsersRepository
from app.repositories.database import db_session


class TestUsersRepository(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        db_session.remove()

    def test_get_all(self):
        configuration = ConfigurationComponent()
        repository = UsersRepository(configuration)
        user = UserEntity("cambio")
        repository.create(user)

        data = UserEntity.query.all()

        frame = repository.list()
        data = frame.to_dict()
        self.assertTrue(data)
        frame = repository.get_one(data[0]["user_id"])
        data = frame.to_dict()
        repository.delete_one(data[0]["user_id"])
        self.assertTrue(data)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
