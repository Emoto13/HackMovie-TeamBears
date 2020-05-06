import hashlib
from templates.templates_log_in import get_login_info
from verification.verification_check_log_in_info import check_log_in_info
from decorators.decorators_log_in import check_if_logged_in


@check_if_logged_in
def log_in(factory):
    name, password = get_login_info()
    hashed_password = hash_password(password, name)
    check_log_in_info([name, hashed_password])
    print('You logged in successfully!')
    factory.user_name = name
    factory.is_logged_in = True


def hash_password(password, salt):
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)
    return hashed_password
