# Answers:

#   Line 1: output = 12
#   Smallest number = 5
#   Largest number = 20

#   Line 2: output = 5
#   Smallest number = 3
#   Highest number = 9
#   Line 2 could not have produced a 4 as the random.randrange starts on 3 with steps of 2 making the only viable outputs 3, 5 ,7 and 9

#   Line 3: output = 4.930915566359118
#   Smallest number = 2.5
#   Largest number = 5.5

from random import randint
print(randint(1, 100))