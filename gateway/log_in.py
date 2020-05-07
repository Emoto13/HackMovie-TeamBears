import sqlite3
from utils.constants.queries_check_log_in_info import CHECK_LOG_IN_INFO
from utils.database_communication import DataBaseCommunication


def get_log_in_info(user_name, hashed_password):
    connection = sqlite3.connect('database.db')
    user_info = DataBaseCommunication.get_data(connection, CHECK_LOG_IN_INFO, user_name, hashed_password)
    return user_info
