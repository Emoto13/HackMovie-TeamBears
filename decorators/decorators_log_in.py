def check_if_logged_in(func):
    def factory_wraper(factory):
        if factory.is_logged_in:
            raise ValueError('You are already logged in?!')
        func(factory)
    return factory_wraper
