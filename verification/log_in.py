def verify_user_exists(user_info):
    if not user_info:
        raise ValueError('Wrong user name or password')
