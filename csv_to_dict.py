import csv

file = 'oscar.csv'
with open(file) as fh:
    rd = csv.DictReader(fh, delimiter=',')
    for row in rd:
        print(row['Name'])
