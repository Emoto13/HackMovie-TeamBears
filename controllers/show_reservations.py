from gateway.show_reservations import get_reservations
from views.templates.show_reservations import display_reservations
from models.view_models.reservation import ReservationViewModel


def show_reservations(user_name):
    reservations_raw_data = get_reservations(user_name)
    reservations = map_reservations(reservations_raw_data)
    display_reservations(reservations)


def map_reservations(reservations_raw_data):
    return list(map(lambda props: ReservationViewModel.create_model(props), reservations_raw_data))
