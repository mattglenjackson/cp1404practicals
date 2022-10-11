"""
MIN_NUMBER = 1
MAX_NUMBER = 45
AMOUNT_OF_NUMBERS_PER_QUICK_PICK = 6

get number_of_quick_picks

for i in number_of_quick_picks
    numbers = []
    for j in range AMOUNT_OF_NUMBERS_PER_QUICK_PICK
        number = random integer between MIN_NUMBER and MAX_NUMBER
        while number is in numbers
            number = random integer between MIN_NUMBER and MAX_NUMBER
        append number to numbers
        sort numbers in numerical order
    print numbers in message with spacing formatting
"""

from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 45
AMOUNT_OF_NUMBERS_PER_QUICK_PICK = 6

number_of_quick_picks = int(input("How many quick picks? "))

for i in range(number_of_quick_picks):
    numbers = []
    for j in range(AMOUNT_OF_NUMBERS_PER_QUICK_PICK):
        number = randint(MIN_NUMBER, MAX_NUMBER)
        while number in numbers:
            number = randint(MIN_NUMBER, MAX_NUMBER)
        numbers.append(number)
        numbers.sort()
    print("{:2} {:2} {:2} {:2} {:2} {:2}".format(*numbers))
