"""Default parameter in functions"""

def print_line(length=2, pen='-'):
    """Print a line of pen characters"""
    print(pen * length)



print_line(pen = '*') # set 2nd parameter, and uses default first parameter

# UNPACK TUPLE for function
# def format_date(day, month, year):
#   return f"{day}/{month}/{year}"
#
# date = (22, 11, 1988)  # tuple
# format_date(*date)     # unpacks date tuple
# format_date(date)      # error: month & year unfilled
#
# FUNCTION ANNOTATIONS AND TESTABILITY
# def print_line(length: int, pen: str) -> None:         return type
#
# SRP follow single responsibility principle
# TESTABILITY
#
# for age in range(101):
#   category = determine_category(age)
#   print(f"{age} is {category}")
#
# ABOVE, TESTS 100 TIMES and prints RESULT OF FUNCTION
#
# FUNCTIONS harder to test when input/output inside function(when doesn't need to be functions purpose)
#
#
#
#