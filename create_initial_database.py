import sqlite3
from constants.queries_initial_database import movie_query_init, projections_query_init, users_query_init, \
    reservations_query_init, movie_query_fill


def main():
    queries = [
        movie_query_init,
        projections_query_init,
        users_query_init,
        reservations_query_init,
        movie_query_fill
    ]

    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    for query in queries:
        cursor.execute(query)
    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
