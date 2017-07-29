import csv
with open('data.csv', encoding='utf-8') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        print(row)
