from typing import abstractmethod


class BaseFrame:

    def __init__(self):
        pass

    @abstractmethod
    def get_metadata(self): pass

    @abstractmethod
    def get_schema(self): pass

    @abstractmethod
    def load_data(self, data): pass

    @abstractmethod
    def to_dict(self, orient="records"): pass
