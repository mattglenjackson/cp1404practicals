"""
Estimated time: 2h
Actual time:
"""
from project import Project

MENU = "(L)oad Projects\n(S)ave Projects\n(D)isplay Projects\n(F)ilter Projects by Date" \
       "\n(A)dd New Project\n(U)pdate Project"
FILENAME = "projects.txt"


def main():
    print(MENU)
    projects = load_projects(FILENAME)
    choice = input('>>> ').upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter filename: ")
            load_projects(filename)
        elif choice == "S":
            print("Save Projects")
        elif choice == "D":
            for project in projects:
                print(project)
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


def load_projects(filename):
    """Load projects from filename."""
    projects = []
    in_file = open(filename, 'r')
    in_file.readline()  # Remove header from filename
    for line in in_file:
        parts = line.strip().split("\t")
        projects.append(Project(parts[0], parts[1], parts[2], parts[3], parts[4]))
    return projects


main()
