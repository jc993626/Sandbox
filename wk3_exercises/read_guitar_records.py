with open("guitar_list.txt", "r") as in_file:
    for line in in_file:
        parts = line.strip().split(',')
        guitar_brand = parts[0]
        year_made = int(parts[1])
        price = float(parts[2].replace("\\n", ""))
        print(f"The guitar brand {guitar_brand}, made in {year_made}, has a value of ${price}")


# will not strip \n


