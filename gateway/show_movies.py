from utils.constants.queries_show_movies import GET_MOVIES
from utils.database_communication import DataBaseCommunication


def get_movies():
    movies = DataBaseCommunication.get_entries(GET_MOVIES)
    return movies
