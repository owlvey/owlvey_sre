#  https://wakatime.com/blog/32-flask-part-1-sqlalchemy-models-to-json

import json

from sqlalchemy.orm.attributes import QueryableAttribute


class BaseEntity:

    __tablename__ = None

    def __init__(self):
        pass

    def _read_fields(self):
        return list()

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def from_kwargs(self, **kwargs):
        """Update this model with a dictionary."""
        _force = kwargs.pop("_force", False)

        readonly = self._read_fields()

        columns = self.__table__.columns.keys()
        relationships = self.__mapper__.relationships.keys()
        properties = dir(self)

        changes = {}

        for key in columns:
            if key.startswith("_"):
                continue
            allowed = True if _force or key not in readonly else False
            exists = True if key in kwargs else False
            if allowed and exists:
                val = getattr(self, key)
                if val != kwargs[key]:
                    changes[key] = {"old": val, "new": kwargs[key]}
                    setattr(self, key, kwargs[key])

        return changes

    def from_dict(self, data):
        """Update this model with a dictionary."""
        readonly = self._read_fields()

        columns = self.__table__.columns.keys()
        relationships = self.__mapper__.relationships.keys()
        properties = dir(self)

        changes = {}

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
        default = self._default_fields if hasattr(self, "_default_fields") else []
        columns = self.__table__.columns.keys()
        ret_data = {}
        for key in columns:
            if key.startswith("_"):
                continue
            if key in _hide or key in hidden:
                continue
            ret_data[key] = getattr(self, key)
        return ret_data

