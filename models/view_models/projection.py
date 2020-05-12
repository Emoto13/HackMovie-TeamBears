from models.abstract_model import AbstractModel


class ProjectionViewModel(AbstractModel):
    def __init__(self, projection_id=None, projection_type=None, date=None, time=None, seats_left=None,
                 movie_name=None, movie_rating=None, movie_id=None):
        self.projection_id = projection_id
        self.projection_type = projection_type
        self.date = date
        self.time = time
        self.seats_left = seats_left

        self.movie_id = movie_id
        self.movie_name = movie_name
        self.movie_rating = movie_rating

