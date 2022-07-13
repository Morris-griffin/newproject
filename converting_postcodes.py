import csv
file = open('somewhere.csv')
type(file)
csvreader = csv.reader(file)
search = input("what postcode do you want to see")
post= csv.DictReader(file)
line_count = 0
for row in post:
    if row["pcd"]== search:
        print(row["lat"],row["long"])
