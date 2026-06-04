
with open("data.txt", "r") as in_file:
    in_file.readline() #ignores header, reads 1st line, then for loops reads the rest
    for line in in_file:
        #print(line)
        parts = line.strip().split(',')

        #print(parts)
        name = parts[0]
        age = int(parts[1])
        print(f"{name} will be {age+1} years old next year")




