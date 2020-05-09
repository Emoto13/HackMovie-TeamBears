from utils.create_initial_database import create_initial_database
from utils.global_helpers import is_command_exit, clear_screen
from views.templates.get_command import get_command
from views.templates.introduction import display_introduction
from views.client_factory import ClientCommandFactory


def main():
    display_introduction()
    create_initial_database()
    factory = ClientCommandFactory()

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
