from models.abstract_model import AbstractModel


class Projection(AbstractModel):
    def __init__(self, projection_id=None,  movie_id=None, projection_type=None, date=None, time=None):
        self.projection_id = projection_id
        self.movie_id = movie_id
        self.projection_type = projection_type
        self.date = date
        self.time = time
