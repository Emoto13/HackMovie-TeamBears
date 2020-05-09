from models.abstract_model import AbstractModel


class Projection(AbstractModel):
    def __init__(self, projection_id=None, projection_type=None, date='', time=None):
        super().__init__()
        self.projection_id = projection_id
        self.projection_type = projection_type
        self.date = date
        self.time = time

    @classmethod
    def create_model(cls, props):
        return cls(projection_id=props['id'],
                   projection_type=props['type'],
                   date=props['date'],
                   time=props['time'])

