import sqlite3
from utils.constants.queries_remove_from_table import DELETE_FROM_TABLE


def remove_reservation(reservation_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(DELETE_FROM_TABLE, [reservation_id])
    connection.commit()
    connection.close()
