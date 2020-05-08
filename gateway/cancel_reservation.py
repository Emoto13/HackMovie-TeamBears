from utils.constants.queries_cancel_reservation import DELETE_FROM_TABLE, GET_ALL_RESERVATIONS_BY_USER_NAME
from utils.database_communication import DataBaseCommunication


def remove_reservation(reservation_id):
    DataBaseCommunication.update_database(DELETE_FROM_TABLE, reservation_id)


def get_all_reservations_by_user_name(user_name):
    reservations = DataBaseCommunication.get_data(GET_ALL_RESERVATIONS_BY_USER_NAME, user_name)
    return reservations
