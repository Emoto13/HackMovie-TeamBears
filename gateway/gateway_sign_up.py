import sqlite3
from constants.queries_sign_up import USER_NAME_UNIQUENESSS, ADD_USER_TO_DATABASE


def check_user_name(user_name):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(USER_NAME_UNIQUENESSS, user_name)
    name = cursor.fetchall()
    connection.commit()
    connection.close()
    return name


def add_user_to_database(user_name, password):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(ADD_USER_TO_DATABASE, [user_name, password])
    name = cursor.fetchall()
    connection.commit()
    connection.close()
    return name
