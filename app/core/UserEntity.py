from sqlalchemy import Column, ForeignKey, Integer, String
from app.core.BaseEntity import BaseEntity
from app.core.QueryEntity import QueryEntity


class UserEntity(BaseEntity, QueryEntity):

    __tablename__ = "Users"

    email = Column(String(256), nullable=False, unique=True)

    def __init__(self, email=None):
        super().__init__()
        self.email = email

    def _read_fields(self):
        return UserEntity.id.name

