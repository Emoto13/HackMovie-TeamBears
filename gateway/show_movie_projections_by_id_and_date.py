from utils.database_communication import DataBaseCommunication
from utils.constants.queries_show_movie_projections_by_id_and_date import GET_PROJECTIONS_BY_MOVIE_ID,\
    GET_PROJECTIONS_BY_MOVIE_ID_AND_DATE


def get_movies_by_id_or_date(movie_id, date):
    if date is None:
        return get_movies_by_id(movie_id)
    return get_movies_by_id_and_date(movie_id, date)


def get_movies_by_id(movie_id):
    movies = DataBaseCommunication.get_entries(GET_PROJECTIONS_BY_MOVIE_ID, movie_id)
    return movies


def get_movies_by_id_and_date(movie_id, date):
    movies = DataBaseCommunication.get_entries(GET_PROJECTIONS_BY_MOVIE_ID_AND_DATE, movie_id, date)
    return movies
