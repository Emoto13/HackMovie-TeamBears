import re


# Step 2
def verify_projections_with_empty_seats_exist(projections):
    if len(projections) == 0:
        raise ValueError("Sorry no projections with empty seats found. :'( ")

# Step 4
def seat_is_valid(seat, saloon):
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
    return True


def verify_seat_input(row_and_column):
    if row_and_column is None:
        print('Error wrong input. Correct input is in the form of (number, number)')
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
def action_is_invalid(action, actions):
    if action not in actions.keys():
        print("No such action")
        return False
    return True
