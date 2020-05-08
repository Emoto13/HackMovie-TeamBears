from verification.sign_up import verify_user_name_uniqueness, verify_password


def sign_up_name():
    while True:
        user_name = input('Type desired user_name: ')
        if verify_user_name_uniqueness(user_name):
            return user_name


def sign_up_password():
    while True:
        password = input('Type desired password: ')
        verification_password = input('Type password again: ')
        if verify_password(password, verification_password):
            return password
