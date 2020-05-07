import sqlite3
from utils.constants.queries_create_database import QUERY_MOVIE_INIT, QUERY_PROJECTIONS_INIT, QUERY_USERS_INIT, \
    QUERY_RESERVATIONS_INIT
from utils.database_communication import DataBaseCommunication


def create_initial_database():
    queries = [
        QUERY_MOVIE_INIT,
        QUERY_PROJECTIONS_INIT,
        QUERY_USERS_INIT,
        QUERY_RESERVATIONS_INIT,
    ]

    connection = sqlite3.connect('database.db')
    for query in queries:
        DataBaseCommunication.update_database(connection, query)
