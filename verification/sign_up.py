from gateway.sign_up import check_user_name_already_exists
from views.templates.sign_up_display import display_incorrect_verification_password, display_incorrect_password_length,\
    display_incorrect_uppercase_format, display_incorrect_special_char_format, display_user_name_is_taken
import string


# TODO Rename to predicates
def is_user_name_unique(user_name):
    user_names_found = check_user_name_already_exists(user_name)
    if user_names_found:
        display_user_name_is_taken()
        return False
    return True


def are_passwords_matching(password, verification_password):
    if is_password_secure(password, verification_password):
        return True
    return False


def is_password_secure(password, verification_password):
    special_char = set(string.punctuation)
    if password != verification_password:
        display_incorrect_verification_password()
        return False
    if len(password) < 8:
        display_incorrect_password_length()
        return False
    if not any(char.isupper() for char in password):
        display_incorrect_uppercase_format()
        return False
    if not any(char in special_char for char in password):
        display_incorrect_special_char_format()
        return False
    return True
