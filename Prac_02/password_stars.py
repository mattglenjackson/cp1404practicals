def main():
    """main program"""
    password = get_password()

    print_asterix(password)


def get_password():
    """Get password from user."""
    password = input("Enter Password: ")
    while len(password) <= 5:
        print("Password must be longer than 5 characters")
        password = input("Enter Password: ")
    return password


def print_asterix(password):
    """print line of asterix, password characters long."""
    print("*" * len(password))


main()
