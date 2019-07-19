from app.core.BaseEntity import BaseEntity
from app.repositories.database import db_session


class EntityRepository:

    def __init__(self):
        pass

    def create(self, data: BaseEntity):
        db_session.add(data)
        db_session.commit()

    def delete(self, data: BaseEntity):
        db_session.delete(data)
        db_session.commit()

    def update(self, data: BaseEntity):
        db_session.commit()

