import pandas as pd

from app.core.BaseFrame import BaseFrame


class UsersFrame(BaseFrame):

    def __init__(self):
        super().__init__()
        self._frame = pd.DataFrame(columns=self.get_metadata())

    def get_metadata(self):
        return ["user_id", "email"]

    def get_schema(self):
        return "Users"

    def add(self, name):
        self._frame = self._frame.append(data, ignore_index=True)

    def load_data(self, data):
        self._frame = pd.DataFrame(data, columns=self.get_metadata())

    def to_dict(self, orient="records"):
        return self._frame.to_dict(orient=orient)

    def __str__(self):
        print(self._frame.head())
        return "ok"
