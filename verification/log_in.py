def verify_user_exists(user_info):
    if len(user_info) == 0:
        raise ValueError('Wrong user name or password')
