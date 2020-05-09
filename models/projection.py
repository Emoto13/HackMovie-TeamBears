from models.abstract_model import AbstractModel


class Projection(AbstractModel):
    def __init__(self, projection_id=None, projection_type=None, date='', time=None, seats_left=None,
                 movie_name=None, rating=None):
        self.projection_id = projection_id
        self.projection_type = projection_type
        self.date = date
        self.time = time
        self.seats_left = seats_left
        self.movie_name = movie_name
        self.rating = rating

    def __str__(self):
        return f"[{self.projection_id}] - {self.date if self.date else ''} {self.time} ({self.projection_type}) " \
               f"{str(self.seats_left) + ' seats left' if self.seats_left else ''}"

    @classmethod
    def create_model(cls, props):
        if 'rating' in props.keys():
            return cls(movie_name=props['name'],
                       projection_type=props['type'],
                       date=props['date'],
                       time=props['time'],
                       rating=props['rating'])

        if 'seats_left' in props.keys():
            return cls(projection_id=props['id'],
                       movie_name=props['name'],
                       projection_type=props['type'],
                       date=props['date'],
                       time=props['time'],
                       seats_left=props['seats_left'])

        if 'date' in props.keys():
            return cls(projection_id=props['id'],
                       movie_name=props['name'],
                       projection_type=props['type'],
                       date=props['date'],
                       time=props['time'])

        return cls(projection_id=props['id'],
                   projection_type=props['type'],
                   time=props['time'])
