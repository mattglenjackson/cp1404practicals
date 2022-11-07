from guitar import Guitar

FILENAME = "guitars.csv"
MENU = "(D)isplay Guitars\n(A)dd Guitar\n(Q)uit"


def main():
    """Loads guitars file guitar file, sorts guitars and then displays them."""
    print("Welcome to my guitar program for CP1404.")
    guitars = load_guitars(FILENAME)
    sort_guitars(guitars)
    print(MENU)
    choice = input('>>> ').upper()
    while choice != "Q":
        if choice == "D":
            display_guitars(guitars)
        elif choice == "A":
            add_guitar(guitars)
            sort_guitars(guitars)
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input('>>> ').upper()
    save_guitars(FILENAME, guitars)
    print("Farewell!")


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


def add_guitar(guitars):
    """Add guitar to list of guitars"""
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost $: "))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)


def sort_guitars(guitars):
    """Sort list of guitars."""
    guitars.sort()


def save_guitars(filename, guitars):
    """Save list of guitars to guitars file."""
    out_file = open(filename, 'w')
    for guitar in guitars:
        print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
    out_file.close()


main()
