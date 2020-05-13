from functools import partial

from models.view_models.user import UserViewModel
from verification.factory import verify_command

from controllers.show_movies import show_movies_command
from controllers.show_movie_projections_by_id_and_date import show_movie_projections_by_id_and_date
from controllers.make_reservation import make_reservation
from controllers.show_reservations import show_reservations
from controllers.cancel_reservation import cancel_reservation
from controllers.log_in import log_in
from controllers.sign_up import sign_up
from controllers.exit import exit_command
from controllers.help import get_help_menu


class ClientCommandFactory:
    def __init__(self):
        self.user = None
        self.is_logged_in = False

    def execute_command(self, command_with_arguments):
        # partial is used for functions which take global params as args
        commands = {
            'show_movies': show_movies_command,
            'show_movie_projections': show_movie_projections_by_id_and_date,
            'make_reservation': partial(make_reservation, self.user.user_name),
            'show_reservations': partial(show_reservations, self.user.user_name),
            'cancel_reservation': partial(cancel_reservation, self.user.user_name),
            'log_in': partial(log_in, self),
            'sign_up': partial(sign_up, self),
            'exit': exit_command,
            'help': get_help_menu
        }

        return self.handle_command(command_with_arguments.strip(), commands)

    def handle_command(self, command_with_arguments, commands):
        command_with_arguments = command_with_arguments.split(" ")
        command = command_with_arguments.pop(0)
        arguments = command_with_arguments
        verify_command(command, commands, self.is_logged_in)
        command_to_execute = commands[command]
        return self.execute_command_with_its_arguments(command_to_execute, arguments)

    def execute_command_with_its_arguments(self, command_to_execute, arguments):
        if len(arguments) > 0:
            return command_to_execute(*arguments)
        return command_to_execute()

    def set_logged_user(self, user_name):
        self.user = UserViewModel(user_name)
        self.is_logged_in = True
