from utils.session_context_manager import session_scope
from models.orm_models.movie import User


def get_log_in_info(user_name, hashed_password):
    with session_scope() as session:
        user_info = session.query(User).filter(User.user_name == user_name). \
            filter(User.user_password == hashed_password).all()
    return user_info
