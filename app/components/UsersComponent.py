from app.components.BaseComponent import BaseComponent
from app.core.BaseEntity import BaseEntity
from app.core.UserEntity import UserEntity


class UsersComponent(BaseComponent):

    def __init__(self):
        super().__init__()

    def _build_entity(self) -> BaseEntity:
        return UserEntity()

    def get_by_email(self, email):
        user = UserEntity.query.filter(UserEntity.email == email).first()
        return user.to_dict()
