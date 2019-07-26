from sqlalchemy import Column, ForeignKey, Integer, String
from app.core.BaseEntity import BaseEntity
from app.core.QueryEntity import QueryEntity


class UserEntity(BaseEntity, QueryEntity):

    __tablename__ = "Users"

    email = Column(String(256), nullable=False, unique=True)
    avatar = Column(String(1024), nullable=False)

    def __init__(self):
        super().__init__()

    def create(self, email, avatar=None):
        self.email = email
        self.avatar = avatar or "https://cdn.iconscout.com/icon/free/png-256/avatar-375-456327.png"
        self._validate()

    def _read_fields(self):
        return UserEntity.id.name

