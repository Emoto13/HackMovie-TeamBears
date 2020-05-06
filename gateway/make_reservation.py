import sqlite3
from utils.constants.queries_make_reservation import QUERY_MOVIES_WITH_AVAILABLE_SEATS, QUERY_GET_PROJECTIONS_BY_ID, \
    QUERY_GET_TAKEN_SEATS_BY_ROWS_AND_COLUMNS, QUERY_GET_PROJECTION_INFO, QUERY_GET_USER_ID_BY_USERNAME, \
    QUERY_INSERT_INTO_RESERVATIONS


def get_movies_with_available_seats():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(QUERY_MOVIES_WITH_AVAILABLE_SEATS)
    movies = cursor.fetchall()
    connection.commit()
    connection.close()
    return movies


def get_projections_by_id(movie_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(QUERY_GET_PROJECTIONS_BY_ID, (movie_id,))
    movies = cursor.fetchall()
    connection.commit()
    connection.close()
    return movies


def get_projection_info(projection_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(QUERY_GET_PROJECTION_INFO, (projection_id,))
    projection_info = cursor.fetchall()
    connection.commit()
    connection.close()
    return projection_info


def get_taken_seats_rows_and_columns(projection_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(QUERY_GET_TAKEN_SEATS_BY_ROWS_AND_COLUMNS, (projection_id,))
    rows_and_columns = cursor.fetchall()
    connection.commit()
    connection.close()
    return rows_and_columns


def get_user_id_by_name(user_name):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(QUERY_GET_USER_ID_BY_USERNAME, (user_name,))
    user_id = cursor.fetchall()
    connection.commit()
    connection.close()
    return user_id


def create_new_reservation_in_the_database(user_id, projection_id, seats):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    for seat in seats:
        row = seat[0]
        col = seat[1]
        info = (user_id, projection_id, row, col)
        print(info)
        cursor.execute(QUERY_INSERT_INTO_RESERVATIONS, info)
    connection.commit()
    connection.close()

