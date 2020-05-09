from utils.constants.queries_make_reservation import QUERY_MOVIES_WITH_AVAILABLE_SEATS, QUERY_GET_PROJECTIONS_BY_ID, \
    QUERY_GET_TAKEN_SEATS_BY_ROWS_AND_COLUMNS, QUERY_GET_PROJECTION_INFO, QUERY_GET_USER_ID_BY_USERNAME, \
    QUERY_INSERT_INTO_RESERVATIONS
from utils.database_communication import DataBaseCommunication


def get_movies_with_available_seats():
    movies = DataBaseCommunication.get_entries(QUERY_MOVIES_WITH_AVAILABLE_SEATS)
    return movies


def get_projections_by_id(movie_id):
    movies = DataBaseCommunication.get_entries(QUERY_GET_PROJECTIONS_BY_ID, movie_id)
    return movies


def get_projection_info(projection_id):
    projection_info = DataBaseCommunication.get_single_entry(QUERY_GET_PROJECTION_INFO, projection_id)
    return projection_info


def get_taken_seats_rows_and_columns(projection_id):
    rows_and_columns = DataBaseCommunication.get_entries(QUERY_GET_TAKEN_SEATS_BY_ROWS_AND_COLUMNS,
                                                         projection_id)
    return rows_and_columns


def get_user_id_by_name(user_name):
    user_id = DataBaseCommunication.get_single_entry(QUERY_GET_USER_ID_BY_USERNAME, user_name)
    return user_id


def create_new_reservation_in_the_database(user_id, reservation):
    for seat in reservation.seats:
        row, col = seat[0], seat[1]
        DataBaseCommunication.update_database(QUERY_INSERT_INTO_RESERVATIONS,
                                              user_id,
                                              reservation.projection_id,
                                              row,
                                              col)
