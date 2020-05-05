

def handle_wrapper(command_to_execute, arguments):
    if len(arguments) > 0:
        return command_to_execute(*arguments)
    return command_to_execute()
