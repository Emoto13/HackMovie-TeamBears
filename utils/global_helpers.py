def is_command_exit(command):
    if command == 'exit':
        return True
    return False


def clear_screen():
    input('Press enter to continue...')
    print("\033c", end="")
