from app.components.BaseComponent import BaseComponent
from app.core.BaseEntity import BaseEntity
from app.core.SquadEntity import SquadEntity


class SquadsComponent(BaseComponent):

    def __init__(self):
        super().__init__()

    def _build_entity(self) -> BaseEntity:
        return SquadEntity()

    def get_by_namea(self, name):
        squad = SquadEntity.query.filter(SquadEntity.name == name).first()
        return squad.to_dict()
