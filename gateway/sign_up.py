from utils.session_context_manager import session_scope
from models.orm_models.user import User


def check_user_name_already_exists(user_name):
    with session_scope() as session:
        user_names = session.query(User).filter(User.user_name == user_name).all()
    return user_names


def add_user_to_database(user):
    with session_scope() as session:
        session.add(user)
