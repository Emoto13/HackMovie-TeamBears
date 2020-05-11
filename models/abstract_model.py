from abc import ABC


class AbstractModel(ABC):
    @classmethod
    def create_model(cls, props):
        model = cls()
        for key in model.__dict__.keys():
            if key in props.keys():
                model.__dict__[key] = props[key]
        return model
