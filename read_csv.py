import csv

with open('memo.csv', mode='r', encoding='utf-8', newline='') as csv_file:
    reader = csv.DictReader(csv_file, fieldnames=['date', 'comment'])
    for row in reader:
        print(row['date'], row['comment'])
