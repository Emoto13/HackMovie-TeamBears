from models.abstract_model import AbstractModel


class User(AbstractModel):
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    @classmethod
    def create_model(cls, props):
        return cls(props[''])
