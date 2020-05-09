import sqlite3


class DataBaseCommunication:
    @staticmethod
    def get_single_entry(query, *arguments):
        connection = sqlite3.connect('database.db')
        args_for_query = [arg for arg in arguments]
        try:
            with connection:
                connection.row_factory = sqlite3.Row
                cursor = connection.cursor()
                cursor.execute(query, args_for_query)
                result = cursor.fetchone()
                return result
        except Exception as e:
            print(e)

    @staticmethod
    def get_entries(query, *arguments):
        connection = sqlite3.connect('database.db')
        args_for_query = [arg for arg in arguments]
        try:
            with connection:
                connection.row_factory = sqlite3.Row
                cursor = connection.cursor()
                cursor.execute(query, args_for_query)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(e)

    @staticmethod
    def update_database(query, *arguments):
        connection = sqlite3.connect('database.db')
        args_for_query = [arg for arg in arguments]
        try:
            with connection:
                cursor = connection.cursor()
                cursor.execute(query, args_for_query)
        except Exception as e:
            print(e)
