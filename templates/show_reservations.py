def display_reservations(reservations):
    print('\nYour current reservations are:\n')
    for reservation in reservations:
        reservation_id, name, date, time, projection_type, row, col = reservation
        print(
            f'[{reservation_id}] {name} on date {date} at {time} ({projection_type})'
            f' seat: {row} {col}')
