"""Guessing game with files and exceptions"""

FILENAME = "secret.txt"






def main():
    secret = load_number(FILENAME)
    guess = get_valid_integer()

    while guess != secret:
        print("Guess again!")
        guess = get_valid_integer()
    print("You got it!")


def get_valid_integer():
    is_valid_input = False
    while not is_valid_input:
        try:
            guess = int(input("Guess?"))
            is_valid_input = True
        except ValueError:
            print("Invalid integer")
    return guess # no problem with undefined variable


"""
is_valid_input = False
while not is_valid_input:
    try:
        age = int(input("Age: "))
        if age < 0:
            print("Age must be >= 0")
        else:
            is_valid_input = True
    except ValueError:
        print("Invalid (not an integer)")
"""

def load_number(filename):
    """Load integer from file filename"""

    try:
        infile = open(filename, "r")#added for filename not found error (except FileNotFoundError)
        number = int(infile.read())
    except ValueError:
        print(f"Invalid contents in {filename}")
        number = 5
    except FileNotFoundError
        print(f"{filename} not found")
        number = 4
    else:
        infile.close()
    return number
main()


