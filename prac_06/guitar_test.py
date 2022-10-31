from prac_06.guitar import Guitar


def main():

    # gibson_l5_ces = Guitar("Gibson L-5 CES", 1922)
    # another_guitar = Guitar("Another Guitar", 2013)
    #
    # print(f"{gibson_l5_ces.name} get_age() - Expected 100. Got {gibson_l5_ces.get_age()}")
    # print(f"{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age()}")
    # print(f"{gibson_l5_ces.name} is_vintage() - Expected True. Got {gibson_l5_ces.is_vintage(gibson_l5_ces.get_age())}")
    # print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage(another_guitar.get_age())}")

    guitars = []
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("My guitars!")
    # name = input("Name: ")
    # while name != "":
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: "))
    #     guitars.append(Guitar(name, year, cost))
    #     name = input("Name: ")

    print("These are my guitars: ")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage(guitar.get_age()):
            vintage_string = "(vintage)"
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


main()
