from verification.make_reservation import is_ticket_number_valid, is_movie_id_valid, is_projection_id_valid, \
    seat_is_valid, is_action_valid


def get_ticket_number():
    tickets = int(input('Step 1 (User): Choose number of tickets> '))
    while not is_ticket_number_valid(tickets):
        tickets = int(input('Step 1 (User): Choose number of tickets> '))
    return tickets


def get_movie_id(movie_ids):
    movie_id = int(input('Step 2 (Movie): Choose a movie by id> '))
    while not is_movie_id_valid(movie_id, movie_ids):
        movie_id = int(input('Step 2 (Movie): Choose a movie by id> '))
    return movie_id


def get_projection_id(projection_ids):
    projection_id = int(input('Step 3 (Projection): Choose a projection by id> '))
    while not is_projection_id_valid(projection_id, projection_ids):
        projection_id = int(input('Step 3 (Projection): Choose a projection by id> '))
    return projection_id


def get_seat_number(seat_number, saloon, seats):
    seat = input(f'Step 4 (Seats): Choose seat {seat_number}> ')
    while not seat_is_valid(seat, saloon, seats):
        seat = input(f'Step 4 (Seats): Choose seat {seat_number}> ')
    return seat


def get_action(actions):
    action = input("Step 5 (Confirm - type 'finalize' or 'cancel' to cancel the reservation)> ")
    while not is_action_valid(action, actions):
        action = input("Step 5 (Confirm - type 'finalize' or 'cancel' to cancel the reservation)> ")
    return action
