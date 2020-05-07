from client_factory import ClientCommandFactory


def main():
    command = None
    ccf = ClientCommandFactory()
    while command != 'exit':
        try:
            command = input("Enter command: ")
            ccf.execute_command(command)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
