import csv
with open("jinko.txt") as f:
    reader = csv.reader(f)
    for l in reader:
        print(l)
            