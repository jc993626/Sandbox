
names = ["Lindsay", "Hossein", "Dmitry", "Bruce", "Alan"]
number_of_elements = len(names)
is_valid_input = False
while not is_valid_input:
    try:
        print("Enter the number for the name you wish to select")
        print(f"[0] for {names[0]}, [1] for {names[1]}, [2] for {names[2]}, [3] for {names[3]}, [4] {names[4]}")
        name_to_display = int(input("Enter a number:"))
        if 0 > name_to_display >= number_of_elements :
            print("Invalid selection")
        else:
            is_valid_input = True
    except ValueError:
        print("Invalid number for selection of name")
print(f"The name you selected is {names[name_to_display]}")

# how to have a selection of '1' be [0] index ??





