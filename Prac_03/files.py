"""
get name
open in_file called name.txt
print name in in_file
close in_file

open in_file called name.txt
name = read file
close in_file

open out_file called name.txt
print message with name in out_file
close out_file

FILE_NAME = numbers.txt
open FILE_NAME for reading
total = 0
for line in range 2
    number = integer value of line
    total = total + number
print total
close FILE_NAME

open FILE_NAME for reading
total = 0
for line in FILE_NAME
    number = integer value of line
    total = total + number
print total
close FILE_NAME
"""

name = input("Enter Name: ")

out_file = open(f"{name}.txt", "w")
print(name, file = out_file)
out_file.close()

in_file = open(f"{name}.txt", "r")
name = 0  # To check to see if program is reading files correctly
name = in_file.read().strip()
in_file.close()

out_file = open(f"{name}.txt", "w")
print(f"Your name is {name}", file = out_file)
out_file.close()

FILE_NAME = "numbers.txt"
in_file = open(FILE_NAME, "r")
total = 0
for line in range(2):
    number = int(in_file.readline())
    total += number
print(total)
in_file.close()

in_file = open(FILE_NAME, "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()