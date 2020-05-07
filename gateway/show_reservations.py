import sqlite3
from utils.constants.queries_show_reservations import SHOW_RESERVATIONS
from utils.database_communication import DataBaseCommunication


def get_reservations(name):
    connection = sqlite3.connect('database.db')
    sorted_movies = DataBaseCommunication.get_data(connection, SHOW_RESERVATIONS, name)
    return sorted_movies
