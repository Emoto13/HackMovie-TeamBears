def display_reservations(reservations):
    print('\nYour current reservations are:\n')
    for reservation in reservations:
        print(
            f'{reservation[0]}. {reservation[1]} on date {reservation[2]} at {reservation[3]}'
            f' seat: {reservation[4]}, {reservation[5]}')
    pass
