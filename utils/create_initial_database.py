from utils.constants.queries_create_database import MOVIE_INIT, PROJECTIONS_INIT, USERS_INIT, \
    RESERVATIONS_INIT
from utils.database_communication import DataBaseCommunication


def create_initial_database():
    queries = [
        MOVIE_INIT,
        PROJECTIONS_INIT,
        USERS_INIT,
        RESERVATIONS_INIT,
    ]

    for query in queries:
        DataBaseCommunication.update_database(query)
