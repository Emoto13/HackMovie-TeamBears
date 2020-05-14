import hashlib
from gateway.sign_up import add_user_to_database
from views.templates.sign_up_input import sign_up_name, sign_up_password
from utils.decorators.log_in_decorators import already_logged_in
from models.orm_models.user import User


# TODO refactor
@already_logged_in
def sign_up(factory):
    user_name = sign_up_name()
    user_password = sign_up_password()
    hashed_password = hash_password(user_password, user_name)
    add_user_to_database(User(user_name=user_name, user_password=hashed_password))


def hash_password(user_password, salt):
    hashed_password = hashlib.pbkdf2_hmac('sha256', user_password.encode('utf-8'), salt.encode('utf-8'), 100000)
    return hashed_password
