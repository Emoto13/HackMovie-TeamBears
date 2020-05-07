def greet_user(name):
    print(f'Hello, {name}')


def display_movies_with_available_seats(movies):
    print('Current movies: ')
    for movie in movies:
        print(f'[{movie[0]}] - {movie[1]} {movie[2]}')


def display_projections(projections):
    movie_name = projections[0][1]
    print(f"Projections for movie '{movie_name}': ")
    for projection in projections:
        print(f'[{projection[0]}] - {projection[2]} {projection[3]} {projection[4]} seats left')


def display_saloon_with_taken_seats(saloon):
    for row in saloon:
        print("".join(row))
    print(f'{(" " * (len(saloon)))}SCREEN IS HERE{(" " * (len(saloon)))}')


def display_reservation_info(seats, *projection_info):
    name, rating, date, time, type_of_projection = projection_info

    seats = [str(seat) for seat in seats]

    print('This is your reservation: ')
    print(f"Movie: {name} ({rating})")
    print(f"Date and time: {date} {time} ({type_of_projection})")
    print(f"Seats: {' '.join(seats)}")


def display_successful_reservation():
    print("Reservation is successful. Thanks.")


def display_cancel_reservation():
    print("You have cancelled the reservation!")
