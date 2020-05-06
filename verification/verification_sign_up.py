from gateway.gateway_sign_up import check_user_name
from templates.templates_sign_up import sign_up_name, sign_up_password
import string


def verify_user_name_uniqueness():
    while True:
        user_name = sign_up_name()
        res = check_user_name([user_name])
        if len(res) == 0:
            return user_name
        print('User_name is taken!')


def verify_password():
    while True:
        password, verification_password = sign_up_password()
        if verify_password_params(password, verification_password):
            return password


def verify_password_params(password, verification_password):
    special_char = set(string.punctuation)
    if password != verification_password:
        print('Passwords do not match')
        return False
    if len(password) < 8:
        print('Password should be at least 8 characters')
        return False
    if not any(char.isupper() for char in password):
        print('Password should have at least 1 uppercase char')
        return False
    if not any(char in special_char for char in password):
        print('Password should have at least 1 special char')
        return False
    return True
