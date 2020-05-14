from models.orm_models.reservation import Reservation
from utils.session_context_manager import session_scope


def get_reservations_by_user_id(user_id):
    with session_scope() as session:
        reservations = session.query(Reservation).filter(Reservation.user_id == user_id).all()
    return reservations
