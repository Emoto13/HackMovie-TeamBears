import sqlite3
from utils.constants.queries_sign_up import USER_NAME_UNIQUENESS, ADD_USER_TO_DATABASE
from utils.database_communication import DataBaseCommunication


def check_user_name_already_exists(user_name):
    connection = sqlite3.connect('database.db')
    name = DataBaseCommunication.get_data(connection, USER_NAME_UNIQUENESS, user_name)
    return name


def add_user_to_database(user_name, password):
    connection = sqlite3.connect('database.db')
    name = DataBaseCommunication.get_data(connection, ADD_USER_TO_DATABASE, user_name, password)
    return name
