from utils.bootstrap import bootstrap
from utils.global_helpers import is_command_exit, clear_screen
from views.templates.get_command import get_command
from views.templates.introduction import display_introduction
from router.router import Router


def main():
    bootstrap()
    display_introduction()
    factory = Router()

    command = None
    while not is_command_exit(command):
        clear_screen()
        command = get_command()
        try:
            factory.execute_command(command)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
