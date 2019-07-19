from app.core.UserEntity import UserEntity
from app.core.UsersFrame import UsersFrame
from app.repositories.BaseRepository import BaseRepository
from app.repositories.database import db_session


class UsersRepository(BaseRepository):
    def __init__(self, configuration):
        super().__init__(configuration)

    def list(self):
        frame = UsersFrame()
        return self._list(frame)

    def create(self, user: UserEntity):
        db_session.add(user)
        db_session.commit()

    def get_one(self, key):
        frame = UsersFrame()
        return self._get_one(frame, key)

    def delete_one(self, key):
        frame = UsersFrame()
        return self._delete_one(frame, key)





