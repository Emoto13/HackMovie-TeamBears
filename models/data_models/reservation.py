from models.abstract_model import AbstractModel


class Reservation(AbstractModel):
    def __init__(self, reservation_id=None, projection_id=None, user_id=None, row=None, col=None):
        self.reservation_id = reservation_id
        self.projection_id = projection_id
        self.user_id = user_id
        self.row = row
        self.col = col
