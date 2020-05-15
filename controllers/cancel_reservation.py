from views.templates.cancel_reservation_display import display_cancel_reservation
from views.templates.cancel_reservation_input import get_reservation
from gateway.cancel_reservation import remove_reservation, get_all_reservations_by_user_id


def cancel_reservation(user_id):
    reservation_ids = get_reservations_ids(user_id)
    reservation_id = get_reservation(reservation_ids)
    remove_reservation(reservation_id)
    display_cancel_reservation()


def get_reservations_ids(user_id):
    reservations = get_all_reservations_by_user_id(user_id)
    return list(map(lambda reservation: reservation.reservation_id, reservations))
