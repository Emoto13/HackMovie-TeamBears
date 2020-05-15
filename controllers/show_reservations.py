from gateway.show_reservations import get_reservations_by_user_id
from views.templates.show_reservations import display_reservations


def show_reservations(user_id):
    reservations = get_reservations_by_user_id(user_id)
    display_reservations(reservations)
