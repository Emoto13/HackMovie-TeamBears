import sqlite3
from queries_initial_database import movie_query_init, projections_query_init, users_query_init, reservations_query_init


def main():
    queries = [
        movie_query_init,
        projections_query_init,
        users_query_init,
        reservations_query_init,
    ]

    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    for query in queries:
        cursor.execute(query)
    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
