import csv

with open('daum.csv','r',encoding='utf-8',newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        print(row['rank'],row['value'])