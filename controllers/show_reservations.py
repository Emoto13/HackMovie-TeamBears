from gateway.show_reservations import get_reservations
from views.templates.show_reservations import display_reservations
from models.reservation import Reservation


def show_reservations(user_name):
    reservations_raw_data = get_reservations(user_name)
    reservations = map_reservations(reservations_raw_data)
    display_reservations(reservations)


def map_reservations(reservations):
    return list(map(lambda reservation: Reservation.create_model(reservation), reservations))