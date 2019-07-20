from sqlalchemy import Column, ForeignKey, Integer, String
from app.core.BaseEntity import BaseEntity
from app.core.QueryEntity import QueryEntity


class SubscriptionEntity(BaseEntity, QueryEntity):

    __tablename__ = "Subscriptions"

    customer_id = Column(Integer, ForeignKey('Customers.id'))
    user_id = Column(Integer, ForeignKey('Users.id'))

    def __init__(self):
        super().__init__()

    def _read_fields(self):
        return SubscriptionEntity.id.name

