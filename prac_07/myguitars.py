from guitar import Guitar

FILENAME = "guitars.csv"
MENU = "(D)isplay Guitars\n(A)dd Guitar\n(Q)uit"


def main():
    """Loads guitars file guitar file, sorts guitars and then displays them."""
    guitars = load_guitars(FILENAME)
    sort_guitars(guitars)
    display_guitars(guitars)


def load_guitars(filename):
    """Load list of guitars from guitars file."""
    guitars = []
    in_file = open(filename, "r")
    for line in in_file:
        parts = line.split(',')
        guitars.append(Guitar(parts[0], parts[1], parts[2]))
    in_file.close()
    return guitars


def display_guitars(guitars):
    """Display list of guitars."""
    print("My guitars that I own:")
    for guitar in guitars:
        print(guitar)


def sort_guitars(guitars):
    """Sort list of guitars."""
    guitars.sort()


main()
