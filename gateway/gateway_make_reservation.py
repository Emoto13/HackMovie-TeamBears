import sqlite3
from constants.queries_make_reservation import QUERY_MOVIES_WITH_AVAILABLE_SEATS, QUERY_GET_PROJECTIONS_BY_ID, \
    QUERY_GET_TAKEN_SEATS_BY_ROWS_AND_COLUMNS, QUERY_GET_PROJECTION_INFO


def gateway_get_movies_with_available_seats():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(QUERY_MOVIES_WITH_AVAILABLE_SEATS)
    movies = cursor.fetchall()
    connection.commit()
    connection.close()
    return movies


def gateway_get_projections_by_id(movie_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(QUERY_GET_PROJECTIONS_BY_ID, (movie_id,))
    movies = cursor.fetchall()
    connection.commit()
    connection.close()
    return movies


def gateway_get_projection_info(projection_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(QUERY_GET_PROJECTION_INFO, (projection_id,))
    projection_info = cursor.fetchall()
    connection.commit()
    connection.close()
    return projection_info


def gateway_get_taken_seats_rows_and_columns(projection_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(QUERY_GET_TAKEN_SEATS_BY_ROWS_AND_COLUMNS, (projection_id,))
    rows_and_columns = cursor.fetchall()
    connection.commit()
    connection.close()
    return rows_and_columns

def create_new_reservation_in_the_database(user_name, seats):
    pass