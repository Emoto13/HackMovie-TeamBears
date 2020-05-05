from event_handler import handle_command
from commands.show_movies_command import show_movies_command
from commands.show_movie_projections_by_id_and_date_command import show_movie_projections_by_id_and_date


class ClientCommandFactory:
    def __init__(self, name='Guest', is_logged_in=False):
        self.name = name
        self.is_logged_in = is_logged_in

    def execute_command(self, command_with_arguments):
        commands = {
            'show_movies': show_movies_command,
            'show_movie_projections': show_movie_projections_by_id_and_date,
            'make_reservation': '',
            'cancel_reservation': '',
            'exit': '',
            'help': ''
        }

        return handle_command(command_with_arguments, commands)
