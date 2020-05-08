from gateway.sign_up import check_user_name_already_exists
import string

# TODO Rename to predicates


def verify_user_name_uniqueness(user_name):
    names = check_user_name_already_exists(user_name)
    if len(names) != 0:
        print('User_name is taken!')
        return False
    return True


def verify_password(password, verification_password):
    if verify_password_params(password, verification_password):
        return True
    return False


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
