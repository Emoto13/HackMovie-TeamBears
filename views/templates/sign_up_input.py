from verification.sign_up import is_user_name_unique, are_passwords_matching
from getpass import getpass


def sign_up_name():
    while True:
        user_name = input('Type desired user_name: ')
        if is_user_name_unique(user_name):
            return user_name


def sign_up_password():
    while True:
        password = getpass('Type desired password: ')
        verification_password = getpass('Type password again: ')
        if are_passwords_matching(password, verification_password):
            return password
