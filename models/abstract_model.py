from abc import ABC


class AbstractModel(ABC):
    def __init__(self):
        pass

    @classmethod
    def create_model(cls, props):
        pass
