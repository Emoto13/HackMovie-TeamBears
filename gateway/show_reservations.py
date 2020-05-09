from utils.constants.queries_show_reservations import SHOW_RESERVATIONS
from utils.database_communication import DataBaseCommunication


def get_reservations(name):
    sorted_movies = DataBaseCommunication.get_entries(SHOW_RESERVATIONS, name)
    return sorted_movies
