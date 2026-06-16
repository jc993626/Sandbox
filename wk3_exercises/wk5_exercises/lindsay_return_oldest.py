""" do this now, with lindsay"""

def find_oldest(names, ages):
    #return names[ages.index(max(ages))]
    #or
    oldest_age = -1
    oldest_index = -1
    for i, age in enumerate(ages):
        if age > oldest_age:
            oldest_age = age
            oldest_index = i
    return names[oldest_index]

def run_tests():
    i = 0
    names = ["Bill", "Jane", "Sven", "Max"]
    ages = [21, 34, 56, 0]
    #print(names[i], "is", ages[i], "years old")
    print(find_oldest(names, ages))

run_tests()