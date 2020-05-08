from utils.constants.queries_log_in import CHECK_LOG_IN_INFO
from utils.database_communication import DataBaseCommunication


def get_log_in_info(user_name, hashed_password):
    user_info = DataBaseCommunication.get_data(CHECK_LOG_IN_INFO, user_name, hashed_password)
    return user_info
