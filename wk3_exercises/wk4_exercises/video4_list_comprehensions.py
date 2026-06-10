# LIST COMPREHENSIONS
# short cut way to make a new list
# [number for number in numbers]
# [number * 2 for number in numbers]
# [number // 2 for number in numbers]
# [number ** 2 for number in numbers]
# [1 for number in numbers] replaces all numbers with 1
# [print(number) for number in numbers]   dont do, returns 'None'
# USE list comprehension for expressions, eg . *, **, /, //
#[number for number in numbers if number > 50]  = [64, 99, 200]
# neg_numbers = [number for number in numbers if number < 0] assign negative numbers to new list
# [number / 2 for number in numbers if number < 0] half of negative numbers
# [1 / number for number in numbers if number > 10]  gives decimal numbers
# [(1, number) for number in numbers] makes tuple of each number with (1, number)
# WORDS  ********************************
# [word for word in words]
# [word for word in words if len(word) > 5] words greater than 5 characters
# [len(word) for word in words]   length of all words
# max([len(word) for word in words])  max word length in list
# max([len(word) for word in words if len(word) < 5]) if word is less than 5 characters
# [word[0] for word in words]     FIRST letter in each word
# [word.upper() for word in words] makes all words upper case
# [word for word in words if word.isupper()]   ONLY words that have uppercase (all char are uppercase)
# [word for word in words if word[0] in "aeiou"] does not return words starting with 'I'
# [word for word in words if word[0] in "aeiouAEIOU"] OR [word for word in words if word[0].lower() in "aeiou"]
# DATA
# [pair for pair in data]
#[tuple(pair) for pair in data] = [('Derek', 7), ('Carrie', 8), ('Bob', 6), ('Asron', 9)] conv pair to tuple
# [f"{pair[0]} {pair[1]}" for pair in data] JOINS as one string
# max([pair[1] for pair in data]) MAX  score dont need list -> max((pair[1] for pair in data))
# sorted([pair[0] for pair in data if pair[1] > 7]) gives ->['Asron', 'Carrie'] scores > 7
# SUMMARY
# date_strong = input("Enter DOB (d/m/y)")
# parts = date_string.split("/")
# my_dob = (int(parts[0]), int(parts[1]), int(parts[2]))
# SIMPLER
# parts = date_string.split("/")
# my_dob = tuple([int(part) for part in parts])
# MULTIPLE COLLECTS (nested loops)
# [ x + y for x in range(1, 4) for y in range (1, 4)]
#SAME AS
# things = []
# for x in range(1, 4):
#     for y in range(1,4):
#         things.append(x + y)
#
# max([len(word) for word in words])
# max((len(word) for word in words))  does not create and store list. GENERATOR EXPRESSION
