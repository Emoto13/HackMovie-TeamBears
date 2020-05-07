from gateway.show_reservations import get_reservations
from views.templates.show_reservations import display_reservations


def show_reservations(name):
    reservations = get_reservations(name)
    display_reservations(reservations)
