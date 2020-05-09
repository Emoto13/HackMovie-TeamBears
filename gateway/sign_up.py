from utils.constants.queries_sign_up import USERS_WITH_THE_SAME_USER_NAME, ADD_USER_TO_DATABASE
from utils.database_communication import DataBaseCommunication


def check_user_name_already_exists(user_name):
    names = DataBaseCommunication.get_entries(USERS_WITH_THE_SAME_USER_NAME, user_name)
    return names


def add_user_to_database(user_name, password):
    name = DataBaseCommunication.get_entries(ADD_USER_TO_DATABASE, user_name, password)
    return name
