"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
from random import randint


def main():
    """Main function for scores.py."""
    score = get_score()
    grade = determine_grade(score)
    print(grade)

    random_grade = random.randint(0, 100)
    grade = determine_grade(random_grade)
    print(grade)

def determine_grade(score):
    """Determines grade."""
    if score < 0 or score > 100:
        grade = "Invalid grade"
    elif score >= 90:
        grade = "Excellent"
    elif score >= 50:
        grade = "Passable"
    else:
        grade = "Bad"
    return grade


def get_score():
    """Get score from user."""
    score = float(input("Enter score: "))
    return score


main()
