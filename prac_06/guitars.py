from prac_06.guitar import Guitar


def main():
    """Get information about users guitars and print information."""
    guitars = []
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) :${cost:.2f} added.")
        print()
        name = input("Name: ")

    print("These are my guitars: ")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year:>4}), worth ${guitar.cost:10,.2f} {vintage_string}")
        #  I tried multiple attempts to get the guitar name spacing working using
        #  list comprehensions but couldn't figure it out in the end as I kept getting errors with generator expressions
        #  max_name_length = max(len(guitar.name for guitar in guitars))

main()
