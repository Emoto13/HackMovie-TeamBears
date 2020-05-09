from abc import ABC, abstractmethod


class AbstractModel(ABC):
    @classmethod
    @abstractmethod
    def create_model(cls, props):
        pass
