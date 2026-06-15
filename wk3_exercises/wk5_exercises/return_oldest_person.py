""" DO this NOW!"""


names = [("Brett"), ("Matt"), ("Warren"), ("Scotty"), ("Tommy"), ("Jared")]
ages = [(49), (50), (48), (50), (45), (36)]

def main():
    name = check_oldest_person(names, ages)
    print(name)


def check_oldest_person(name_list, age_list):
    index_of_oldest = age_list.index(max(age_list))
    return name_list[index_of_oldest]


main()