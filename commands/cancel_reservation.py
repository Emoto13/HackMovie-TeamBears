from templates.cancel_reservation import get_reservation, display_cancel_reservation
from gateway.cancel_reservation import remove_reservation, get_all_reservations_by_user_name


def cancel_reservation(user_name):
    all_reservations = get_reservations(user_name)
    reservation_id = get_reservation(all_reservations)
    remove_reservation(reservation_id)
    display_cancel_reservation()


def get_reservations(user_name):
    all_reservations = get_all_reservations_by_user_name(user_name)
    return list(map(lambda reservation: reservation[0], all_reservations))
