def sign_up_name():
    user_name = input('Type desired user_name: ')
    return user_name


def sign_up_password():
    password = input('Type desired password: ')
    verification_password = input('Type password again: ')
    return password, verification_password
