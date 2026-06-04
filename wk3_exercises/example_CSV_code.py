with open(filename, 'r', newline='', encoding='utf-8-sig') as in_file:
    reader = csv.reader(in_file)
    next(reader)  # ignore csv header line
    for row in reader:
        print(row)

