from abc import ABC


class AbstractModel(ABC):
    @classmethod
    def create_model(cls, props):
        model = cls()
        model.__dict__ = {key: value for key, value in dict(props).items()}
        return model

#        for key in props.keys():
#            model.__dict__[key] = props[key]
