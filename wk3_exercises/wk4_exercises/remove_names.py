names = ["Ada", "Alan", "Bill", "John"]
print(", ".join(names))

name_to_remove = input("What name do you want to remove? ")
while name_to_remove != "":
    try:
        names.remove(name_to_remove)
    except ValueError:
        print("wrong")
        if not names:
            break
        name_to_remove = input("What name do you want to remove? ")
print(names)