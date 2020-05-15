def greet_user(user_name):
    print(f'Hello, {user_name}')


def display_movies_with_available_seats(movies):
    print('Current movies: ')
    for movie in movies:
        print(f"[{movie.movie_id}] - {movie.movie_name} ({movie.movie_rating})")


def display_projections(projections):
    movie_name = projections[0].movie.movie_name
    print(f"Projections for movie '{movie_name}': ")
    for projection in projections:
        print(
            f"[{projection.projection_id}] - {projection.projection_date} {projection.projection_time} ({projection.projection_type}) "
            f"{get_seats_left(projection)} seats left")


def get_seats_left(projection):
    total_seats = 100
    taken_seats = len(projection.reservations)
    return total_seats - taken_seats


def display_saloon_with_taken_seats(saloon):
    for row in saloon:
        print("".join(row))


def display_reservation_info(projection_info, seats):
    display_seats = [str(seat) for seat in seats]

    print('This is your reservation: ')
    print(f"Movie: {projection_info.movie.movie_name}")
    print(
        f"Date and time: {projection_info.projection_date} {projection_info.projection_time} ({projection_info.projection_type})")
    print(f"Seats: {' '.join(display_seats)}")


def display_successful_reservation():
    print("Reservation is successful. Thanks.")


def display_cancel():
    print("You have cancelled the reservation of tickets!")


def display_wrong_movie_id():
    print("No movie with this id. Try again.")


def display_wrong_projection_id():
    print("No projections for this movie with such id. Try again.")


def display_seat_already_reserved():
    print("You already choose this seat")


def display_wrong_seat_input():
    print("Error wrong input. Correct input is in the form of (number, number)")


def display_seat_is_not_in_the_saloon():
    print("No such seat in the saloon.")


def display_seat_is_taken():
    print("Seat is taken. Please, choose another one.")


def display_no_such_action():
    print("No such command/action.")


def display_invalid_tickets():
    print("Invalid number of tickets. Try again.")
