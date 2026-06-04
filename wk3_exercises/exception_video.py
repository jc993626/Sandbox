# all input is evil until proven otherwise

# try:
#     suite
# except ErrorType:
#     suite
#-----------------------------
#error in TRY, matches error to exception
#----------------------------
#except:    UNBOUND exception most general, comes last. *** NOT good practice!! ***
    #print(" some other exception happened")   error

"""
valid_input = False
while not valid_input:
    try:
        age = int(input("age: ")
        valid_input = True
    except ValueError:
        print("Invalid (not an integer)"
print("Next year you will be", age + 1)
"""
# LABEL ALL EXCEPTIONS (read error messages)

# try:
#   value = int("no"))
# except ValueError as error:  (assigns error message to variable 'error')
#   print(error)

# print(repr(error)) get message and text

















