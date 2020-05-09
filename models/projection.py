from models.abstract_model import AbstractModel


class Projection(AbstractModel):
    def __init__(self, projection_id=None, projection_type=None, date='', time=None, seats_left=None,
                 movie_name=None, movie_rating=None):
        self.projection_id = projection_id
        self.projection_type = projection_type
        self.seats_left = seats_left
        self.movie_name = movie_name
        self.movie_rating = movie_rating
        self.date = date
        self.time = time

    @classmethod
    def create_model(cls, props):
        return super().create_model(props)
