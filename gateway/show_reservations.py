from utils.constants.queries_show_reservations import GET_RESERVATIONS
from utils.database_communication import DataBaseCommunication


def get_reservations(name):
    sorted_movies = DataBaseCommunication.get_entries(GET_RESERVATIONS, name)
    return sorted_movies
