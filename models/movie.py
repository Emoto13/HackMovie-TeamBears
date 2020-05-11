from models.abstract_model import AbstractModel


class Movie(AbstractModel):
    def __init__(self, movie_id=None, movie_name=None, movie_rating=None):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.movie_rating = movie_rating
