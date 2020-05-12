from abc import ABC


class AbstractModel(ABC):
    @classmethod
    def create_model(cls, props):
        model = cls()
        for key in props.keys():
            if hasattr(model, key):
                setattr(model, key, props[key])
        return model
