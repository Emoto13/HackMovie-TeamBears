import re
from functools import partial

from constants.saloon import SALOON
from gateway.gateway_make_reservation import gateway_get_movies_with_available_seats, gateway_get_projections_by_id, \
    gateway_get_taken_seats_rows_and_columns, gateway_get_projection_info, create_new_reservation_in_the_database

from templates.templates_make_reservation import *
from verification.verification_make_reservation import seat_is_valid, action_is_invalid, \
    verify_projections_with_empty_seats_exist


# TODO finish finish_reservation
def make_reservation(user_name):
    greet_user(user_name)

    # Step 1
    tickets = choose_tickets_number_and_display_movies()

    # Step 2
    choose_movie_by_id_and_display_projections()

    # Step 3
    saloon_and_projection_info = choose_projection_by_id_and_display_salon()
    saloon, projection_info = saloon_and_projection_info[0], saloon_and_projection_info[1]

    # Step 4
    seats = choose_seats_and_display_reservation(tickets, saloon, projection_info)

    # Step 5
    finish_reservation(user_name, seats)


def choose_tickets_number_and_display_movies():
    tickets = int(input('Step 1 (User): Choose number of tickets> '))  # verify tickets
    movies = gateway_get_movies_with_available_seats()
    display_movies_with_available_seats(movies)
    return tickets


def choose_movie_by_id_and_display_projections():
    movie_id = int(input('Step 2 (Movie): Choose a movie by id> '))  # verify movie_id
    projections = gateway_get_projections_by_id(movie_id)
    verify_projections_with_empty_seats_exist(projections)
    display_projections(projections)
    return projections


def choose_projection_by_id_and_display_salon():
    projection_id = int(input('Step 3 (Projection): Choose a projection by id> '))
    # verify projection_by_id

    taken_seats_rows_and_columns = gateway_get_taken_seats_rows_and_columns(projection_id)
    projection_info = gateway_get_projection_info(projection_id)
    saloon = generate_saloon(taken_seats_rows_and_columns)
    display_saloon_with_taken_seats(saloon)
    return saloon, projection_info


def generate_saloon(taken_seats_rows_and_columns):
    saloon = SALOON
    for row_and_column in taken_seats_rows_and_columns:
        row = row_and_column[0]
        col = row_and_column[1]
        saloon[row][col] = '  X'
    return saloon


def choose_seats_and_display_reservation(tickets, saloon, projection_info):
    seats = choose_seats(tickets, saloon)
    display_reservation_info(projection_info, seats)
    return seats


def choose_seats(tickets, saloon):
    seats = []
    for i in range(tickets):
        seat = input('Step 4 (Seats): Choose seat 1> ')
        while not seat_is_valid(seat, saloon):
            seat = input('Step 4 (Seats): Choose seat 1> ')
        seats.append(get_row_and_col(seat))
    return seats


def get_row_and_col(seat):
    regex = '[(]?([\\d]+),[ ]*([\\d]+)[)]?'
    row_and_column = re.search(regex, seat)
    row = int(row_and_column.group(1))
    col = int(row_and_column.group(2))
    return row, col


def finish_reservation(user_name, seats):
    action = input("Step 5 (Confirm - type 'finalize' or 'cancel' to cancel the reservation)> ")
    actions = {'finalize': partial(finalize, user_name, seats),
               'cancel': ''}

    return actions[action]


def handle_action(action, actions):
    while action_is_invalid(action, actions):
        action = input("Step 5 (Confirm - type 'finalize' or 'cancel' to cancel the reservation)> ")
    return actions[action]


def finalize(user_name, seats):
    create_new_reservation_in_the_database(user_name, seats)


def cancel():
    display_cancel_reservation()
