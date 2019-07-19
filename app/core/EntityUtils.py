from typing import List

from app.core.BaseEntity import BaseEntity


class EntityUtils:

    @staticmethod
    def entities_to_list_dictionaries(data: List[BaseEntity]):
        result = list()
        for item in data:
            result.append(item.as_dict())
        return result

