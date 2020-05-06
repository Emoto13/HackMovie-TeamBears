import re
from functools import partial

from utils.constants import SALOON
from verification.make_reservation import seat_is_valid, action_is_invalid, \
    verify_projections_with_empty_seats_exist

from gateway.make_reservation import *
from templates.make_reservation import *


def make_reservation(user_name):
    greet_user(user_name)

    # Step 1
    tickets = choose_tickets_number_and_display_movies()

    # Step 2
    choose_movie_by_id_and_display_projections()

    # Step 3
    saloon_and_projection_info = choose_projection_by_id_and_display_salon()
    saloon, projection_info, projection_id = \
        saloon_and_projection_info[0], saloon_and_projection_info[1], saloon_and_projection_info[2]

    # Step 4
    seats = choose_seats_and_display_reservation(tickets, saloon, projection_info)

    # Step 5
    finish_reservation(user_name, projection_id, seats)


def choose_tickets_number_and_display_movies():
    tickets = int(input('Step 1 (User): Choose number of tickets> '))  # verify tickets
    movies = get_movies_with_available_seats()
    display_movies_with_available_seats(movies)
    return tickets


def choose_movie_by_id_and_display_projections():
    movie_id = int(input('Step 2 (Movie): Choose a movie by id> '))
    # verify movie_id
    projections = get_projections_by_id(movie_id)
    verify_projections_with_empty_seats_exist(projections)
    display_projections(projections)
    return projections


def choose_projection_by_id_and_display_salon():
    projection_id = int(input('Step 3 (Projection): Choose a projection by id> '))
    # verify projection_by_id

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


def finish_reservation(user_name, projection_id,  seats):
    action = input("Step 5 (Confirm - type 'finalize' or 'cancel' to cancel the reservation)> ")
    actions = {'finalize': partial(finalize, user_name, projection_id, seats),
               'cancel': cancel}

    return handle_action(action, actions)


def handle_action(action, actions):
    while not action_is_invalid(action, actions):
        action = input("Step 5 (Confirm - type 'finalize' or 'cancel' to cancel the reservation)> ")
    return actions[action]()


def finalize(user_name, projection_id,  seats):
    user_id = int(get_user_id_by_name(user_name)[0][0])
    create_new_reservation_in_the_database(user_id, projection_id, seats)
    display_successful_reservation()


def cancel():
    display_cancel_reservation()
