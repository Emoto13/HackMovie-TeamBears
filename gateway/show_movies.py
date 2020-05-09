from utils.constants.queries_show_movies import SHOW_MOVIES_QUERY
from utils.database_communication import DataBaseCommunication


def get_movies():
    movies = DataBaseCommunication.get_entries(SHOW_MOVIES_QUERY)
    return movies
