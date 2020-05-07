from templates.cancel_reservation_display import display_incorrect_reservation_id


def is_reservation_id_valid_or_user_wants_to_go_back(command, reservation_ids):
    if command == 'back':
        raise Exception('You cancelled the command.')
    reservation_id = int(command)
    if reservation_id not in reservation_ids:
        display_incorrect_reservation_id()
        return False
    return True
