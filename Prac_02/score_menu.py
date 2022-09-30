"""
MENU = (E)nter score (P)rint result Print (S)tar (Q)uit

function main
    score = -1
    print MENU
    get choice
    while choice != "Q"
        if choice = "E"
            score = call get_valid_score function
        else if choice = "P"
            grade = call determine_grade function
            print grade
        else if choice = "S"
            call print_stars function
        else
            print "Invalid input"

        print MENU
        get choice
    print farewell message


function get_valid_score
    get score
    while score < 0 or score > 100
        print "Invalid score"
        get score
    return score


function determine_grade(score):
    if score = -1
        grade = "Please enter a score"
    elif score >= 90
        grade = "Excellent"
    elif score >= 50
        grade = "Passable"
    else
        grade = "Bad"
    return grade


function print_stars(score)
    print "*" score times


call main
"""

MENU = "(E)nter score\n(P)rint result\nPrint (S)tar\n(Q)uit"


def main():
    """Score_menu.py main function."""
    score = -1
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "E":
            score = get_valid_score()
        elif choice == "P":
            grade = determine_grade(score)
            print(grade)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid input")

        print(MENU)
        choice = input(">>> ").upper()

    print("Farewell")


def get_valid_score():
    """Get valid score from user."""
    score = int(input("Enter Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter Score: "))
    return score


def determine_grade(score):
    """Determines grade of users score."""
    if score == -1:
        grade = "Please enter a score"
    elif score >= 90:
        grade = "Excellent"
    elif score >= 50:
        grade = "Passable"
    else:
        grade = "Bad"
    return grade


def print_stars(score):
    """Prints line of asterix, score length long."""
    print("*" * score)


main()
