import sqlite3
from utils.constants.queries_remove_from_table import DELETE_FROM_TABLE
from utils.database_communication import DataBaseCommunication


def remove_reservation(reservation_id):
    connection = sqlite3.connect('database.db')
    DataBaseCommunication.update_database(connection, DELETE_FROM_TABLE, reservation_id)
