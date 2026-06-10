# builtin functions - len, min, max, sum
# eg. max(list) will not work if one element is a string

#remove element
# del scores[1] BY INDEX
#or
# scores.remove(1) BY VALUE if more than one 1, removes first.
#scores.append(item) add item to end
# scores.sort() sort elements in asc order
#scores.reverse() reverses order of elements in list
#scores.count(1)  count values of those specified

#letters = sorted('hi mum')
#sorted(letters)

#things[5] = 0
#things[5] += 1  modify [5] by 1, things[5] now = 1(0+1)
#things.insert(index, value)
# eg. things.insert(0, 1) inserts 1 at start of list

#IN and NOT IN
# eg if 2 IN things:
# 1 in things
# "a" in "aeiou"

#list_of_course = ["CP1401", "CP1404", "CP2406"]
#for subject in list_of_course: recognises that subject are the elements of subjects
#    print(subject)
# for singular in plural

# dont have to return list from function, not with mutable objects
# def main():
#     numbers = [1, 2, 3]
#     add_offset(numbers, 2)
#     print(numbers)                NUMBERS and ELEMENTS are alias' refering to same object

# def add_offset(elements, offset):
#     for i in range(len(elements)):
#         elements[i] += offset

#NESTED lists
# eg. data =[['derek', 7], [], []]
# things = ['a', [1, 2, 3], 'z']
# things[1][0]
from operator import itemgetter

from docutils.utils.punctuation_chars import delimiters
from pygments.lexer import words

#data = [['derek', 7], ['carrie', 8], ['bob', 6], ['aaron', 9]]
#data.sort()
#data.sort(key=itemgetter(1), reverse=True) #default sort is asc, reverse=True is desc order
#for record in data:
#    print(record)

# import random
# random.shuffle(things)

#SPLIT
#things.split()
#things.split(',')  ',' delimiters

#JOIN join strings
#     words[i] = words[i].title()  capitalise each words
# text = ', '.join(words)          puts comma between words

# words = 'one two three'.split()
# print(words)                          CANNOT USE 'for word in words' as index must be integer not str
# for i in range(len(words)):
#     words[i] = words[i].title()
# text = ', '.join(words)
# print(text)
 # strings are sequences too
 #what works with lists works with STRINGS









