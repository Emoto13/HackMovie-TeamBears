import sqlite3
from utils.constants.queries_show_reservations import SHOW_RESERVATIONS


def get_reservations(name):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(SHOW_RESERVATIONS, [name])
    sorted_movies = cursor.fetchall()
    connection.commit()
    connection.close()

    return sorted_movies
