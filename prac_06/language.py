"""
Estimate: 30 mins
Actual: 45 mins - First I had __int__ instead of __init__ as my constructor so my class didn't work.
                  Then I struggled with creating a list as I didn't realise that printing the list
                  (trying to check outputs were correct) would give me expressions such as
                  "<prac_06.programming_language.ProgrammingLanguage object at 0x00000267D2F92350>" instead of what I
                  had typically seen before we started OOP.
                  Learnt lots from this particular practical task.
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)
    languages = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
