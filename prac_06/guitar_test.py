from prac_06.guitar import Guitar


def main():
    """Test program for Guitar class."""
    gibson_l5_ces = Guitar("Gibson L-5 CES", 1922)
    another_guitar = Guitar("Another Guitar", 2013)

    print(f"{gibson_l5_ces.name} get_age() - Expected 100. Got {gibson_l5_ces.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age()}")
    print(f"{gibson_l5_ces.name} is_vintage() - Expected True. Got {gibson_l5_ces.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")


main()
