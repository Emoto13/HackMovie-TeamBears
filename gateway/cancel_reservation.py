from models.reservation import Reservation
from utils.session_context_manager import session_scope


def remove_reservation(reservation_id):
    with session_scope() as session:
        session.query(Reservation).filter(Reservation.reservation_id == reservation_id).delete(
            synchronize_session=False)


def get_all_reservations_by_user_id(user_id):
    with session_scope() as session:
        reservations = session.query(Reservation) \
            .filter(Reservation.user_id == user_id) \
            .with_entities(Reservation.reservation_id) \
            .all()
    return reservations

