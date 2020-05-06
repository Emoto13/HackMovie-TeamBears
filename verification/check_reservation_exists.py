from gateway.show_reservations import get_reservations


def check_reservation_exists(name, reservation_id):
    reservations = get_reservations(name)
    for reservation in reservations:
        print(type(reservation[0]))
        if reservation_id == reservation[0]:
            return True
    return False
