from models.abstract_model import AbstractModel


class Reservation(AbstractModel):
    def __init__(self, reservation_id=None, movie_name=None, date=None, time=None, projection_type=None,
                 row=None, col=None, seats=None, projection_id=None):
        self.reservation_id = reservation_id
        self.row = row
        self.col = col
        self.seats = seats

        self.projection_id = projection_id
        self.projection_type = projection_type
        self.date = date
        self.time = time

        self.movie_name = movie_name
