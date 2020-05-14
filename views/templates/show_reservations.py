def display_reservations(reservations):
    print('Your current reservations are:')
    for reservation in reservations:
        print(f'[{reservation.reservation_id}] {reservation.projection.movie.movie_name} '
              f'on date {reservation.projection.projection_date} '
              f'at {reservation.projection.projection_time} ({reservation.projection.projection_type}) '
              f'Seat: {reservation.reservation_row} {reservation.reservation_col}')
