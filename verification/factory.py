from utils.constants.commands_requiring_log_in import COMMANDS_REQUIRING_LOG_IN


def verify_command(command, commands, user_is_logged_in):
    verify_command_exists(command, commands)
    verify_command_requiring_log_in(command, user_is_logged_in)


def verify_command_exists(command, commands):
    if command not in commands.keys():
        raise ValueError("No such command! Try again.")


def verify_command_requiring_log_in(command, user_is_logged_in):
    if command in COMMANDS_REQUIRING_LOG_IN and not user_is_logged_in:
        raise ValueError("Please log in to use this command.")
