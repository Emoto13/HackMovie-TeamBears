import sqlite3
from utils.database_communication import DataBaseCommunication
from utils.constants.queries_show_movie_projections_by_id_and_date import HOW_PROJECTIONS_BY_MOVIE_ID,\
    SHOW_PROJECTIONS_BY_MOVIE_ID_AND_DATE


def show_movies_by_id_or_date(movie_id, date):
    if date is None:
        show_movies_by_id(movie_id)
    show_movies_by_id_and_date(movie_id, date)


def show_movies_by_id(movie_id):
    connection = sqlite3.connect('database.db')
    movies = DataBaseCommunication.get_data(connection, HOW_PROJECTIONS_BY_MOVIE_ID, movie_id)
    return movies


def show_movies_by_id_and_date(movie_id, date):
    connection = sqlite3.connect('database.db')
    movies = DataBaseCommunication.get_data(connection, SHOW_PROJECTIONS_BY_MOVIE_ID_AND_DATE, movie_id, date)
    return movies
