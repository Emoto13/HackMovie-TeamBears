from utils.constants.queries_sign_up import USER_NAME_UNIQUENESS, ADD_USER_TO_DATABASE
from utils.database_communication import DataBaseCommunication


def check_user_name_already_exists(user_name):
    names = DataBaseCommunication.get_data(USER_NAME_UNIQUENESS, user_name)
    return names


def add_user_to_database(user_name, password):
    name = DataBaseCommunication.get_data(ADD_USER_TO_DATABASE, user_name, password)
    return name
