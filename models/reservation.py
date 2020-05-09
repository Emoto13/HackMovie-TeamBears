from models.abstract_model import AbstractModel


class Reservation(AbstractModel):
    def __init__(self, reservation_id=None, name=None, date=None, time=None, projection_type=None, row=None, col=None):
        super().__init__()
        self.reservation_id = reservation_id
        self.name = name
        self.date = date
        self.time = time
        self.projection_type = projection_type
        self.row = row
        self.col = col

    @classmethod
    def create_model(cls, props):
        return cls(reservation_id=props['id'],
                   name=props['name'],
                   date=props['date'],
                   time=props['time'],
                   projection_type=props['type'],
                   row=props['row'],
                   col=props['col'])

    def __str__(self):
        return f'[{self.reservation_id}] {self.name} on date {self.date} at {self.time} ({self.projection_type})\n' \
               f'seat: {self.row} {self.col}\n'
