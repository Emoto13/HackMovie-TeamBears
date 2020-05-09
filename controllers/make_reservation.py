import re
from functools import partial

from models.movie import Movie
from models.projection import Projection
from models.reservation import Reservation
from views.templates.make_reservation_input import get_ticket_number, get_movie_id, get_projection_id, get_seat_number, \
    get_action
from utils.constants.saloon import SALOON
from verification.make_reservation import verify_projections_with_empty_seats_exist

from gateway.make_reservation import *
from views.templates.make_reservation_display import *


def make_reservation(user_name):
    greet_user(user_name)

    # Step 1
    tickets_and_movie_ids = choose_tickets_number_and_get_current_movies()
    tickets, movie_ids = tickets_and_movie_ids['tickets'], tickets_and_movie_ids['ids']

    # Step 2
    projection_ids = choose_movie_by_id_and_get_projections(movie_ids)

    # Step 3
    saloon_and_projection_id = choose_projection_by_id_and_display_salon(projection_ids)
    saloon, projection_id = saloon_and_projection_id['saloon'], saloon_and_projection_id['projection_id']

    # Step 4
    reservation = choose_seats_and_display_reservation(tickets, saloon, projection_id)

    # Step 5
    finish_reservation(user_name, reservation)


def choose_tickets_number_and_get_current_movies():
    tickets = get_ticket_number()

    movies_raw_data = get_movies_with_available_seats()
    movies = map_movies(movies_raw_data)
    display_movies_with_available_seats(movies)

    movie_ids = get_movie_ids(movies)
    return {'tickets': tickets, 'ids': movie_ids}


def map_movies(movies_raw_data):
    return list(map(lambda props: Movie.create_model(props), movies_raw_data))


def get_movie_ids(movies):
    return list(map(lambda movie: movie.movie_id, movies))


def choose_movie_by_id_and_get_projections(movie_ids):
    movie_id = get_movie_id(movie_ids)
    projections_raw_data = get_projections_by_id(movie_id)
    projections = map_projections(projections_raw_data)

    verify_projections_with_empty_seats_exist(projections)
    display_projections(projections)

    projection_ids = get_projection_ids(projections)
    return projection_ids


def map_projections(projections_raw_data):
    return list(map(lambda props: Projection.create_model(props), projections_raw_data))


def get_projection_ids(projections):
    return list(map(lambda projection: projection.projection_id, projections))


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


def choose_seats_and_display_reservation(tickets, saloon, projection_id):
    seats = choose_seats(tickets, saloon)
    projection_info_raw_data = get_projection_info(projection_id)

    reservation_props = dict(**dict(projection_info_raw_data), **{'seats': seats, 'projection_id': projection_id})
    reservation = Reservation.create_model(reservation_props)

    display_reservation_info(reservation)
    return reservation


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


def finish_reservation(user_name, reservation):
    actions = {'finalize': partial(finalize, user_name, reservation),
               'cancel': cancel}
    action = get_action(actions)

    return actions[action]()


def finalize(user_name, reservation):
    user_id = get_user_id_by_name(user_name)['id']
    create_new_reservation_in_the_database(user_id, reservation)
    display_successful_reservation()


def cancel():
    display_cancel()
