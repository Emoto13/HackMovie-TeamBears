from abc import ABC


class AbstractModel(ABC):
    @classmethod
    def create_model(cls, props):
        model = cls()
        for key in props.keys():
            model.__dict__[key] = props[key]
        return model
