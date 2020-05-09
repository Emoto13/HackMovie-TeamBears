from models.abstract_model import AbstractModel


class Reservation(AbstractModel):
    def __init__(self, reservation_id=None, movie_name=None, date=None, time=None, projection_type=None,
                 row=None, col=None, seats=None, projection_id=None):
        self.reservation_id = reservation_id
        self.projection_id = projection_id
        self.movie_name = movie_name
        self.date = date
        self.time = time
        self.projection_type = projection_type
        self.row = row
        self.col = col
        self.seats = seats

    def __str__(self):
        if self.seats:
            display_seats = [str(seat) for seat in self.seats]
            return f"Movie: {self.movie_name}\n" \
                   f"Date and time: {self.date} {self.time} ({self.projection_type})\n" \
                   f"Seats: {' '.join(display_seats)}"

        return f'[{self.reservation_id}] {self.movie_name} on date {self.date} at {self.time} ' \
               f'({self.projection_type})' \
               f'seat: {self.row} {self.col}'

    @classmethod
    def create_model(cls, props):
        if 'seats' in props.keys():
            return cls(movie_name=props['name'],
                       date=props['date'],
                       time=props['time'],
                       projection_type=props['type'],
                       seats=props['seats'],
                       projection_id=props['projection_id'])

        return cls(reservation_id=props['id'],
                   movie_name=props['name'],
                   date=props['date'],
                   time=props['time'],
                   projection_type=props['type'],
                   row=props['row'],
                   col=props['col'])
