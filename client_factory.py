from utils.constants import COMMANDS_REQUIRING_LOG_IN
from commands.show_movies_command import show_movies_command
from commands.show_movie_projections_by_id_and_date_command import show_movie_projections_by_id_and_date
from commands.make_reservation_command import make_reservation
from commands.log_in_command import log_in
from commands.sign_up_command import sign_up
from functools import partial


class ClientCommandFactory:
    def __init__(self, user_name='Guest', is_logged_in=False):
        self.user_name = user_name
        self.is_logged_in = is_logged_in

    def execute_command(self, command_with_arguments):
        # partial is used for functions which take global params as args
        commands = {
            'show_movies': show_movies_command,
            'show_movie_projections': show_movie_projections_by_id_and_date,
            'make_reservation': partial(make_reservation, self.user_name, self.is_logged_in),
            'show_reservations': '',
            'cancel_reservation': '',
            'log_in': partial(log_in, self),
            'sign_up': sign_up,
            'exit': '',
            'help': ''
        }

        return self.handle_command(command_with_arguments, commands)

    # TODO add verification decorator and login decorator
    def handle_command(self, command_with_arguments, commands):
        command_with_arguments = command_with_arguments.split(" ")
        command = command_with_arguments.pop(0)
        arguments = command_with_arguments

        # TODO Refactor to function or decorator
        if command not in commands.keys():
            raise ValueError("No such command! Try again.")

        # TODO Refactor to function or decorator
        if command in COMMANDS_REQUIRING_LOG_IN and not self.is_logged_in:
            raise ValueError("Please log in to use this command.")

        command_to_execute = commands[command]
        return self.handle_wrapper(command_to_execute, arguments)

    def handle_wrapper(self, command_to_execute, arguments):
        if len(arguments) > 0:
            return command_to_execute(*arguments)
        return command_to_execute()
