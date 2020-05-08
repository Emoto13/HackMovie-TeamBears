def already_logged_in(func):
    def factory_wrapper(factory):
        if factory.is_logged_in:
            raise ValueError('You cannot execute this while logged in')
        func(factory)
    return factory_wrapper
