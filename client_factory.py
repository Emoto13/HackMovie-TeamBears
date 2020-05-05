from event_handler import handle_command


class ClientCommandFactory:
    def __init__(self, name='Guest', is_logged_in=False):
        self.name = name
        self.is_logged_in = is_logged_in

    def execute_command(self, command_with_arguments):
        commands = {
            'show_movies': '',
            'show_movie_projections': '',
            'make_reservation': '',
            'cancel_reservation': '',
            'exit': '',
            'help': ''
        }

        return handle_command(command_with_arguments, commands)
