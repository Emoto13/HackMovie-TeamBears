import sqlite3
from utils.constants import QUERY_MOVIE_INIT, QUERY_PROJECTIONS_INIT, QUERY_USERS_INIT, \
    QUERY_RESERVATIONS_INIT, QUERY_USERS_FILL


def main():
    queries = [
        QUERY_MOVIE_INIT,
        QUERY_PROJECTIONS_INIT,
        QUERY_USERS_INIT,
        QUERY_RESERVATIONS_INIT,
        QUERY_USERS_FILL
    ]

    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    for query in queries:
        cursor.execute(query)
    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
