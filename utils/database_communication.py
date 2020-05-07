from contextlib import contextmanager


class DataBaseCommunication:
    @staticmethod
    def get_data(connection, query, *arguments):
        print(arguments)
        args_for_query = [arg for arg in arguments]
        print(args_for_query)
        try:
            with connection:
                cursor = connection.cursor()
                cursor.execute(query, args_for_query)
                result = cursor.fetchall()
                print(result)
                return result
        except Exception as e:
            print(e)


