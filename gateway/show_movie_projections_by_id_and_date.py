import sqlite3


def show_movies_by_id_and_date(query, arguments):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(query, arguments)
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result
