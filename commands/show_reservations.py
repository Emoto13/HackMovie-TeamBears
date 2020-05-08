from gateway.show_reservations import get_reservations
from views.templates.show_reservations import display_reservations


def show_reservations(user_name):
    reservations = get_reservations(user_name)
    display_reservations(reservations)
