def main():
    """Create dictionary of email to names."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        choice = input(f"Is your name {name}? (Y/n) ").upper()
        if choice != "Y" and choice != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

        # if choice == "Y" or choice == "":
        #     email_to_name[email] = name
        # else:
        #     name = input("Name: ")
        #     email_to_name[email] = name
        # email = input("Email: ")

    for email in email_to_name:
        print(f"{email_to_name[email]} ({email})")


def get_name_from_email(email):
    """Extract expected name from email address."""
    # name = " ".join(email[:email.find("@")].split(".")).title()
    prefix = email.split("@")[0]
    parts = prefix.split(".")
    name = " ".join(parts).title()
    return name


main()
