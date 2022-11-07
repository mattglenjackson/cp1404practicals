"""
Estimated time: 2h
Actual time:
"""
from project import Project

MENU = "L - Load Projects\nS - Save Projects\nD - Display Projects\nF - Filter Projects by Date" \
       "\nA - Add New Project\nU - Update Project"


def main():
    print("Welcome to the project management program, select a menu choice below.")
    print(MENU)
    choice = input('>>> ').upper()
    while choice != "Q":
        if choice == "L":
            print("Load Projects")
        elif choice == "S":
            print("Save Projects")
        elif choice == "D":
            print("Display Projects")
        elif choice == "F":
            print("Filter Projects by Date")
        elif choice == "A":
            print("Add New Project")
        elif choice == "U":
            print("Update Project")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input('>>> ').upper()


main()
