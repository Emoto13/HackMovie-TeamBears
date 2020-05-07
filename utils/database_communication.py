class DataBaseCommunication:
    @staticmethod
    def get_data(connection, query, *arguments):
        args_for_query = [arg for arg in arguments]
        try:
            with connection:
                cursor = connection.cursor()
                cursor.execute(query, args_for_query)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(e)

    @staticmethod
    def update_database(connection, query, *arguments):
        args_for_query = [arg for arg in arguments]
        try:
            with connection:
                cursor = connection.cursor()
                cursor.execute(query, args_for_query)
        except Exception as e:
            print(e)
