from getpass import getpass


def get_login_info():
    print('Login to cinema')
    user_name = input('Enter user_name: ')
    password = getpass('Enter password: ')
    return user_name, password


def display_successful_login():
    print('You logged in successfully!')
