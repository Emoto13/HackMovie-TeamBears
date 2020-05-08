from verification.make_reservation import is_ticket_number_valid, is_movie_id_valid, is_projection_id_valid, \
    seat_is_valid, is_action_valid


def get_ticket_number():
    while True:
        tickets = int(input('Step 1 (User): Choose number of tickets> '))
        if is_ticket_number_valid(tickets):
            return tickets


def get_movie_id(movie_ids):
    while True:
        movie_id = int(input('Step 2 (Movie): Choose a movie by id> '))
        if is_movie_id_valid(movie_id, movie_ids):
            return movie_id


def get_projection_id(projection_ids):
    while True:
        projection_id = int(input('Step 3 (Projection): Choose a projection by id> '))
        if is_projection_id_valid(projection_id, projection_ids):
            return projection_id


def get_seat_number(seat_number, saloon, seats):
    while True:
        seat = input(f'Step 4 (Seats): Choose seat {seat_number}> ')
        if seat_is_valid(seat, saloon, seats):
            return seat


def get_action(actions):
    while True:
        action = input("Step 5 (Confirm - type 'finalize' or 'cancel' to cancel the reservation)> ")
        if is_action_valid(action, actions):
            return action
