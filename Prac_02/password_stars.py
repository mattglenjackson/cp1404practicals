password = input("Enter Password: ")

while len(password) <= 5:
    print("Password must be longer than 5 characters")
    password = input("Enter Password: ")

print("*" * len(password))