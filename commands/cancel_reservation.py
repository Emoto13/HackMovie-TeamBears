from templates.choose_reservation_to_cancel import chosen_reservation
from verification.check_reservation_exists import check_reservation_exists
from gateway.remove_reservation import remove_reservation


# TODO improve functionality
def cancel_reservation(name):
    reservation_id = chosen_reservation()
    if not check_reservation_exists(name, reservation_id):
        raise ValueError("Provided id doesn't match any reservation_id")
    remove_reservation(reservation_id)
