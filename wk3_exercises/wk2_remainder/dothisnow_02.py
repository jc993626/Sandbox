"""Complete program, following structure.
menu:
- get valid (non-empty) name
- print greeting with lines
- print secret name (random variation)
"""
import random
from docutils.parsers.rst.directives import length_units


def main():
    name = "Brett"   # testing input, developer speedup, saves entering name each time I test
    print("Menu:")
    choice = input(">").upper()
    while choice != "Q":
        if choice == "G":
            name = get_valid_name()
        elif choice == "P":
            print_greeting(name)
        elif choice == "S":
            print_secret_name(name)
        else:
            print("Invalid choice")
        print("Menu:")
        choice = input(">").upper()
    print("Farewell")


def print_greeting(name):
    length = len(name) # so dont calc length of name twice
    print_line(length)
    print(name)
    print_line(length)


def get_valid_name():
    name = input("Name: ")
    while name == "":
        print("Invalid Name")
        name = input("Name: ")
    return name

def print_line(length):
    print('-' * length)

def print_secret_name(name):
    letters = list(name)
    random.shuffle(letters)
    print("".join(letters))

main()
