#  https://wakatime.com/blog/32-flask-part-1-sqlalchemy-models-to-json
import json
from abc import abstractmethod
from sqlalchemy.orm.attributes import QueryableAttribute
from sqlalchemy import Column, ForeignKey, Integer, String


class BaseEntity:

    id = Column(Integer, primary_key=True, autoincrement=True)

    def __init__(self):
        self._hidden_fields = list()

    def create(self, **kwargs):
        self.from_dict(kwargs)
        self._validate()

    def _read_fields(self):
        return list()

    def from_dict(self, data: dict, force=False, detect_missing=True):
        """Update this model with a dictionary."""
        readonly = self._read_fields()
        if force:
            readonly = list()

        columns = self.__table__.columns.keys()

        changes = {}

        if detect_missing:
            diff = set(data.keys()) - set(columns)
            if diff:
                raise ValueError("{} is missing".format(",".join(diff)))

        for key in columns:
            if key.startswith("_"):
                continue
            allowed = True if key not in readonly else False
            exists = True if key in data else False

            if allowed and exists:
                val = getattr(self, key)
                if val != data[key]:
                    changes[key] = {"old": val, "new": data[key]}
                    setattr(self, key, data[key])

        return changes

    def to_dict(self, _hide=None):
        """Return a dictionary representation of this model."""
        _hide = _hide or list()
        hidden = self._hidden_fields if hasattr(self, "_hidden_fields") else []
        columns = self.__table__.columns.keys()
        ret_data = {}
        for key in columns:
            if key.startswith("_"):
                continue
            if key in _hide or key in hidden:
                continue
            ret_data[key] = getattr(self, key)
        return ret_data

    def _validate(self):
        columns = self.__table__.columns
        for column in columns:
            if column.autoincrement is True:
                pass
            elif not column.nullable and not getattr(self, column.name):
                raise ValueError("{} is null".format(column.name))







