import re


# TODO prints to display in templates
# Step 1
from views.templates.make_reservation_display import display_wrong_movie_id, display_wrong_projection_id, \
    display_seat_already_reserved, display_wrong_seat_input, display_seat_is_not_in_the_saloon, display_seat_is_taken, \
    display_no_such_action


def is_ticket_number_valid(tickets):
    if tickets <= 0:
        print("Invalid number of tickets. Try again.")
        return False
    return True


# Step 2
def is_movie_id_valid(movie_id, movie_ids):
    if movie_id not in movie_ids:
        display_wrong_movie_id()
        return False
    return True


def verify_projections_with_empty_seats_exist(projections):
    if len(projections) == 0:
        raise ValueError("Sorry no projections with empty seats found. :'( ")


# Step 3
def is_projection_id_valid(projection_id, projection_ids):
    if projection_id not in projection_ids:
        display_wrong_projection_id()
        return False
    return True


# Step 4
def seat_is_valid(seat, saloon, seats):
    regex = '[(]?([\\d]+),[ ]*([\\d]+)[)]?'
    row_and_column = re.search(regex, seat)
    if not verify_seat_input(row_and_column):
        return False

    row = int(row_and_column.group(1))
    col = int(row_and_column.group(2))

    if not verify_seat_is_in_saloon(row, col, saloon):
        return False

    if not verify_seat_is_available(row, col, saloon):
        return False

    verifiable_seat = (row, col)

    if verifiable_seat in seats:
        display_seat_already_reserved()
        return False
    return True


def verify_seat_input(row_and_column):
    if row_and_column is None:
        display_wrong_seat_input()
        return False
    return True


def verify_seat_is_in_saloon(row, col, saloon):
    if row < 1 or col < 1 or row >= len(saloon) or col >= len(saloon[0]):
        display_seat_is_not_in_the_saloon()
        return False
    return True


def verify_seat_is_available(row, col, saloon):
    seat = saloon[row][col]
    if seat == '  X':
        display_seat_is_taken()
        return False
    return True


# Step 5
def is_action_valid(action, actions):
    if action not in actions.keys():
        display_no_such_action()
        return False
    return True
