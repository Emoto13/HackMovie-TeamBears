import hashlib
from gateway.sign_up import add_user_to_database
from views.templates.sign_up import sign_up_name, sign_up_password
from utils.decorators.log_in_decorators import already_logged_in


@already_logged_in
def sign_up(factory):
    user_name = sign_up_name()
    password = sign_up_password()
    hashed_password = hash_password(password, user_name)
    add_user_to_database(user_name, hashed_password)


def hash_password(password, salt):
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)
    return hashed_password
