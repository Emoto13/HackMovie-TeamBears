from utils.create_initial_database import create_initial_database
from utils.global_helpers import is_command_exit, clear_screen
from views.templates.introduction import display_introduction
from views.client_factory import ClientCommandFactory

def main():
    display_introduction()
    create_initial_database()
    factory = ClientCommandFactory()

    command = None
    while not is_command_exit(command):
        clear_screen()
        print("You can always type 'help' to display additional information\n")
        command = input("Enter command: ")
        try:
            factory.execute_command(command)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
