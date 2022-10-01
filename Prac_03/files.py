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