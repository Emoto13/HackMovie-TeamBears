import re
from functools import partial

from templates.input_make_reservation import get_ticket_number, get_movie_id, get_projection_id, get_seat_number, \
    get_action
from utils.constants.saloon import SALOON
from verification.make_reservation import verify_projections_with_empty_seats_exist

from gateway.make_reservation import *
from templates.display_make_reservation import *


def make_reservation(user_name):
    greet_user(user_name)

    # Step 1
    tickets, movie_ids = choose_tickets_number_and_display_movies()
    # Step 2
    projection_ids = choose_movie_by_id_and_display_projections(movie_ids)

    # Step 3
    saloon, projection_info, projection_id = choose_projection_by_id_and_display_salon(projection_ids)

    # Step 4
    seats = choose_seats_and_display_reservation(tickets, saloon, projection_info)

    # Step 5
    finish_reservation(user_name, projection_id, seats)


def choose_tickets_number_and_display_movies():
    tickets = get_ticket_number()
    movies = get_movies_with_available_seats()
    display_movies_with_available_seats(movies)
    movie_ids = get_movie_ids(movies)
    return tickets, movie_ids


def get_movie_ids(movies):
    return list(map(lambda movie: movie[0], movies))


def choose_movie_by_id_and_display_projections(movie_ids):
    movie_id = get_movie_id(movie_ids)
    projections = get_projections_by_id(movie_id)
    verify_projections_with_empty_seats_exist(projections)
    display_projections(projections)
    projection_ids = get_projection_ids(projections)
    return projection_ids


def get_projection_ids(projections):
    return list(map(lambda projection: projection[0], projections))


def choose_projection_by_id_and_display_salon(projection_ids):
    projection_id = get_projection_id(projection_ids)
    taken_seats_rows_and_columns = get_taken_seats_rows_and_columns(projection_id)
    projection_info = get_projection_info(projection_id)[0]
    saloon = generate_saloon(taken_seats_rows_and_columns)
    display_saloon_with_taken_seats(saloon)
    return saloon, projection_info, projection_id


def generate_saloon(taken_seats_rows_and_columns):
    saloon = SALOON
    for row_and_column in taken_seats_rows_and_columns:
        row = row_and_column[0]
        col = row_and_column[1]
        saloon[row][col] = '  X'
    return saloon


def choose_seats_and_display_reservation(tickets, saloon, projection_info):
    seats = choose_seats(tickets, saloon)
    display_reservation_info(seats, *projection_info)
    return seats


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


def finish_reservation(user_name, projection_id, seats):
    actions = {'finalize': partial(finalize, user_name, projection_id, seats),
               'cancel': cancel}
    action = get_action(actions)

    return actions[action]()


def finalize(user_name, projection_id, seats):
    user_id = get_user_id_by_name(user_name)
    create_new_reservation_in_the_database(user_id, projection_id, seats)
    display_successful_reservation()


def cancel():
    display_cancel_reservation()
