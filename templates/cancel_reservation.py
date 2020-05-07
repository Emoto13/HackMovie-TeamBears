from verification.cancel_reservation import is_reservation_id_valid


def get_reservation(reservation_ids):
    command = input('Choose a reservation id to cancel or type back to go back: ')
    while not is_reservation_id_valid(command, reservation_ids):
        command = input('Choose a reservation id to cancel or type back to go back: ')
    reservation_id = int(command)
    return reservation_id
