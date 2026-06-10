# TUPLES like lists but different
# IMMUTABLE
# EG date_of_birth = (13, 11, 1945) cannot be changed
# CANNOT modify, index,sum ..etc still work.
# stuff[stuff.index(5)]
# stuff * 2  , multiple by 2, repeats tuple 2 times
#  stuff + 1 wont work.
# stuff + (1,0) concatenate tuple with 1, 0
# 4 in stuff
# 4 not in stuff
# date_of_birth = ( 13, 11, 1945)
# lucky_year = random.randint(1900, 2022)
# if date_of_birth[2] <= lucky_year:
#     print(" congrats old enough")
# functions that return multiple values, return TUPLES
# x,y = (1, 2)  x = 1, y = 2

# def get_low_high(values):
#   return min(values), max(values)

# low, high = get_low_high(things)
# print(low, type(low))

# IF
# z = get_low_high(things)
# print(z, type(z))   (-12, 45) RETURNS a TUPLE

# "-{}-".format(3)
# "-{}-{},{}!".format(stuff[0], stuff[1], stuff[2])
# "-{}-{},{}!".format(*stuff)    takes first 3 index items in stuff
