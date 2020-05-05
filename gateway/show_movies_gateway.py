import sqlite3
from constants.commands_queries import SHOW_MOVIES_QUERY


def show_movies_sorted():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(SHOW_MOVIES_QUERY)
    sorted_movies = cursor.fetchall()
    connection.commit()
    connection.close()

    return sorted_movies
