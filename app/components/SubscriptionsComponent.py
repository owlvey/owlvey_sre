from app.components.BaseComponent import BaseComponent
from app.core.BaseEntity import BaseEntity
from app.core.SubscriptionEntity import SubscriptionEntity


class SubscriptionsComponent(BaseComponent):

    def __init__(self):
        super().__init__()

    def _build_entity(self) -> BaseEntity:
        return SubscriptionEntity()

    def get_by_customer_user(self, customer_id, user_id):
        item = SubscriptionEntity.query.filter(SubscriptionEntity.customer_id == customer_id and
                                               SubscriptionEntity.user_id == user_id).first()
        return item.to_dict()
