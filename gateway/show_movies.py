from utils.constants.queries_show_movies import SHOW_MOVIES_QUERY
from utils.database_communication import DataBaseCommunication


def show_movies_sorted():
    sorted_movies = DataBaseCommunication.get_data(SHOW_MOVIES_QUERY)
    return sorted_movies
