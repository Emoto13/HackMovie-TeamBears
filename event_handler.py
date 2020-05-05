def handle_command(command_with_arguments, commands):
    command_with_arguments = command_with_arguments.split(" ")
    command = command_with_arguments.pop(0)
    arguments = command_with_arguments

    if command not in commands.keys():
        raise ValueError("No such command! Try again.")

    command_to_execute = commands[command]
    return handle_wrapper(command_to_execute, arguments)


def handle_wrapper(command_to_execute, arguments):
    if len(arguments) > 0:
        return command_to_execute(*arguments)
    return command_to_execute()
