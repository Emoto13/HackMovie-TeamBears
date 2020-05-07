from client_factory import ClientCommandFactory
from utils.create_initial_database import create_initial_database
from templates.introduction import display_introduction
from utils.global_helpers import is_command_exit, clear_screen


def main():
    display_introduction()
    create_initial_database()
    factory = ClientCommandFactory()

    command = None
    while not is_command_exit(command):
        clear_screen()
        command = input("Enter command: ")
        try:
            factory.execute_command(command)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
