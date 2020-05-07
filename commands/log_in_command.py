import hashlib
from views.templates.log_in import get_login_info, display_successful_login
from gateway.log_in import get_log_in_info
from utils.decorators.log_in_decorators import already_logged_in
from verification.log_in import verify_user_exists


@already_logged_in
def log_in(factory):
    user_name, password = get_login_info()
    hashed_password = hash_password(password, user_name)

    user_info = get_log_in_info(user_name, hashed_password)
    verify_user_exists(user_info)
    display_successful_login()

    factory.set_logged_user(user_name)


def hash_password(password, salt):
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)
    return hashed_password
