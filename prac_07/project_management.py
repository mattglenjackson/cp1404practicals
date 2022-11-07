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
            add_project(projects)
        elif choice == "U":
            update_project(projects)
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


def add_project(projects):
    """Get project details from user and append to list of projects."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = int(input("Percent complete"))
    projects.append(Project(name, start_date, priority, cost_estimate, percent_complete))


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    choice = int(input("Project Choice: "))
    print(projects[choice])
    new_percentage = int(input("New Percentage: "))
    projects[choice].completion_percentage = new_percentage
    new_priority = int(input("New Priority: "))
    projects[choice].priority = new_priority

main()
