import re
from functools import partial

from utils.constants.saloon import SALOON
from verification.make_reservation import verify_projections_with_empty_seats_exist

from gateway.make_reservation import *
from views.templates.make_reservation_display import *
from views.templates.make_reservation_input import *


def make_reservation(user):
    greet_user(user.user_name)

    # Step 1
    tickets_and_movie_ids = choose_tickets_number_and_get_current_movies()
    tickets, movie_ids = tickets_and_movie_ids['tickets'], tickets_and_movie_ids['movie_ids']

    # Step 2
    projection_ids = choose_movie_by_id_and_get_projections(movie_ids)

    # Step 3
    saloon_and_projection_id = choose_projection_by_id_and_display_salon(projection_ids)
    saloon, projection_id = saloon_and_projection_id['saloon'], saloon_and_projection_id['projection_id']

    # Step 4
    reservations = choose_seats_and_display_reservation(tickets, saloon, projection_id, user.user_id)

    # Step 5
    finish_reservation(reservations)


# Step 1
def choose_tickets_number_and_get_current_movies():
    tickets = get_ticket_number()
    movies = get_movies()
    display_movies_with_available_seats(movies)
    movie_ids = get_movie_ids(movies)
    return {'tickets': tickets, 'movie_ids': movie_ids}


def get_movie_ids(movies):
    return list(map(lambda movie: movie.movie_id, movies))


# Step 2
def choose_movie_by_id_and_get_projections(movie_ids):
    movie_id = get_movie_id(movie_ids)
    projections = get_projections_by_movie_id(movie_id)
    verify_projections_with_empty_seats_exist(projections)
    display_projections(projections)
    projection_ids = get_projection_ids(projections)
    return projection_ids


def get_projection_ids(projections):
    return list(map(lambda projection: projection.projection_id, projections))


# Step 3
def choose_projection_by_id_and_display_salon(projection_ids):
    projection_id = get_projection_id(projection_ids)
    taken_seats_rows_and_columns = get_taken_seats_rows_and_columns(projection_id)
    saloon = generate_saloon(taken_seats_rows_and_columns)
    display_saloon_with_taken_seats(saloon)
    return {'saloon': saloon, 'projection_id': projection_id}


def generate_saloon(taken_seats_rows_and_columns):
    saloon = SALOON
    for row_and_column in taken_seats_rows_and_columns:
        row = row_and_column[0]
        col = row_and_column[1]
        saloon[row][col] = '  X'
    return saloon


# Step 4
def choose_seats_and_display_reservation(tickets, saloon, projection_id, user_id):
    seats = choose_seats(tickets, saloon)
    projection = get_projection_by_projection_id(projection_id)
    display_reservation_info(projection, seats)
    reservations = get_reservations(projection, user_id, seats)
    return reservations


def get_reservations(projection_info, user_id, seats):
    mapping_func = partial(mapping_reservation_function, projection_info, user_id)
    return list(map(lambda seat: mapping_func(seat), seats))


def mapping_reservation_function(projection_info, user_id, seat):
    projection_id = projection_info.projection_id
    row = seat[0]
    col = seat[1]
    return Reservation(projection_id=projection_id, user_id=user_id, reservation_row=row, reservation_col=col)


def choose_seats(tickets, saloon):
    seats = []
    for seat_number in range(1, tickets + 1):
        seat = get_seat_number(seat_number, saloon, seats)
        seats.append(get_row_and_col(seat))
    return seats


def get_row_and_col(seat):
    regex = '[(]?([\\d]+),[ ]*([\\d]+)[)]?'
    row_and_column = re.search(regex, seat)
    row = int(row_and_column.group(1))
    col = int(row_and_column.group(2))
    return row, col


# Step 5
def finish_reservation(reservations):
    actions = {'finalize': partial(finalize, reservations),
               'cancel': cancel}
    action = get_action(actions)

    return actions[action]()


def finalize(reservations):
    create_new_reservation_in_the_database(reservations)
    display_successful_reservation()


def cancel():
    display_cancel()
