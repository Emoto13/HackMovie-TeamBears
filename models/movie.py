from models.abstract_model import AbstractModel


class Movie(AbstractModel):
    def __init__(self, movie_id=None, name=None, rating=None):
        self.movie_id = movie_id
        self.name = name
        self.rating = rating

    @classmethod
    def create_model(cls, props):
        return cls(movie_id=props['id'],
                   name=props['name'],
                   rating=props['rating'])

    def __str__(self):
        return f"[{self.movie_id}] - {self.name} ({self.rating})"
