from app.core.EntityUtils import EntityUtils
from app.core.UserEntity import UserEntity
from app.repositories.EntityRepository import EntityRepository


class UsersComponent:

    def __init__(self):
        self.repository = EntityRepository()

    def create(self, data):
        user = UserEntity()
        user.from_dict(data)
        self.repository.create(user)

    def list(self):
        users = UserEntity.query.all()
        return EntityUtils.entities_to_list_dictionaries(users)

    def get(self, key):
        user = UserEntity.query.filter(UserEntity.user_id == key).first()
        return user.to_dict() if user else None

    def delete(self, key):
        user = UserEntity.query.filter(UserEntity.user_id == key).first()
        self.repository.delete(user)

    def update(self, data):
        user = UserEntity.query.filter(UserEntity.user_id == data[UserEntity.user_id.name]).first()
        user.from_dict(data)
        self.repository.update(user)
        return user.to_dict()
