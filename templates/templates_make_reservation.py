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
    print(f'{(" " * (len(saloon)))}SCREEN IS HERE{(" " * (len(saloon) // 5))}')


def display_reservation_info(projection_info, seats):
    print(projection_info)
    print(seats)


def display_cancel_reservation():
    print("You have cancelled the reservation successfully!")
