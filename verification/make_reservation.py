import re


# TODO prints to display in templates
# Step 1
def is_ticket_number_valid(tickets):
    if tickets <= 0:
        print("Invalid number of tickets. Try again.")
        return False
    return True


# Step 2
def is_movie_id_valid(movie_id, movie_ids):
    if movie_id not in movie_ids:
        print("No movie with this id. Try again.")
        return False
    return True


def verify_projections_with_empty_seats_exist(projections):
    if len(projections) == 0:
        raise ValueError("Sorry no projections with empty seats found. :'( ")


# Step 3
def is_projection_id_valid(projection_id, projection_ids):
    if projection_id not in projection_ids:
        print("No projections for this movie with such id. Try again.")
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
        print("You already choose this seat")
        return False
    return True


def verify_seat_input(row_and_column):
    if row_and_column is None:
        print("Error wrong input. Correct input is in the form of (number, number)")
        return False
    return True


def verify_seat_is_in_saloon(row, col, saloon):
    if row < 1 or col < 1 or row >= len(saloon) or col >= len(saloon[0]):
        print("No such seat in the saloon")
        return False
    return True


def verify_seat_is_available(row, col, saloon):
    seat = saloon[row][col]
    if seat == '  X':
        print("Seat is taken. Please, choose another one.")
        return False
    return True


# Step 5
def is_action_valid(action, actions):
    if action not in actions.keys():
        print("No such action")
        return False
    return True
