
COLOUR_TO_CODE = {'Amber': '#ffbf00', 'Apricot': '#fbceb1', 'Beaver': '#9f8170', 'Bronze': '#cd7f32', 'Corn': '#fbec5d',
                  'Crimson': '#dc143c', 'Denim': '#1560bd', 'Ginger': '#b06500', 'Harlequin': '#3fff00',
                  'Jasmine': '#f8de7e'}

print(COLOUR_TO_CODE)
colour = input("Enter colour name:  ").title()
while colour != "":
    try:
        print(f"Hex code colour for {colour} is {COLOUR_TO_CODE[colour]}")

    except KeyError:
        print("Invalid colour")

    finally:
        colour = input("Enter colour name:  ").title()
