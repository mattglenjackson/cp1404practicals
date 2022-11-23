MENU = "q)uit, c)hoose taxi, d)rive"

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """Taxi simulator main function."""
    total_cost = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'C':
            print("Taxis available:")
            display_taxis(taxis)
            current_taxi = get_taxi_choice(taxis)
        elif choice == 'D':
            if current_taxi is None:
                print('You need to choose a taxi before you can drive')
            else:
                drive_taxi(current_taxi, taxis)
                display_taxi_fare(current_taxi, taxis)
                total_cost += taxis[current_taxi].get_fare()
        else:
            print('Invalid option')
        print(f"Bill to date: {total_cost:,.2f}")
        print(MENU)
        choice = input(">>> ").upper()
    print(f"Total trip cost: ${total_cost}")
    print("Taxis are now:")
    display_taxis(taxis)


def get_taxi_choice(taxis):
    """Get taxi choice from user."""
    choice = int(input('Choose Taxi: '))
    while 0 > choice or choice > (len(taxis) - 1):
        print("Invalid taxi choice")
        choice = int(input('Choose Taxi: '))
    return choice


def display_taxis(taxis):
    """Display taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def drive_taxi(current_taxi, taxis):
    """Get distance from user and drive taxi."""
    distance = int(input("Drive how far? "))
    taxis[current_taxi].start_fare()
    taxis[current_taxi].drive(distance)


def display_taxi_fare(current_taxi, taxis):
    """Display taxi fare."""
    print(f"Your {taxis[current_taxi].name} trip cost you ${taxis[current_taxi].get_fare()}")


if __name__ == '__main__':
    main()
