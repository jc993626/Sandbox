
names = ["Lindsay", "Hossein", "Dmitry", "Bruce", "Alan"]
amount_of_names = len(names)
is_valid_input = False
while not is_valid_input:
    try:
        print("Enter the number for the name you wish to select")
        print(f"[1] for {names[0]}, [2] for {names[1]}, [3] for {names[2]}, [4] for {names[3]}, [5] {names[4]}")
        name_to_display = int(input("Enter a number:"))
        if name_to_display < 0 or name_to_display > amount_of_names:
            print("Invalid selection")
        else:
            is_valid_input = True
    except ValueError:
        print("Invalid number for selection of name")
print(f"The name you selected is {names[name_to_display - 1]}")

# could have used exception  "IndexError"
# fvdf





