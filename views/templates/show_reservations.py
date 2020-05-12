def display_reservations(reservations):
    print('Your current reservations are:')
    for reservation in reservations:
        print(f'[{reservation.reservation_id}] {reservation.movie_name} on date {reservation.date} '
              f'at {reservation.time} ({reservation.projection_type}) '
              f'Seat: {reservation.row} {reservation.col}')
