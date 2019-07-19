import uuid


class DataSeed:

    @staticmethod
    def generate_name(seed):
        return seed.format(uuid.uuid4())

