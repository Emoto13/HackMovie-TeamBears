from models.abstract_model import AbstractModel


class User(AbstractModel):
    def __init__(self, user_name=None, password=None):
        self.user_name = user_name
        self.password = password
