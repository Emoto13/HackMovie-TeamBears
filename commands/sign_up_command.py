import hashlib
from verification.sign_up import verify_user_name_uniqueness, verify_password
from gateway.sign_up import add_user_to_database


def sign_up():
    user_name = verify_user_name_uniqueness()
    password = verify_password()
    hashed_password = hash_password(password, user_name)
    add_user_to_database(user_name, hashed_password)


def hash_password(password, salt):
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)
    return hashed_password
