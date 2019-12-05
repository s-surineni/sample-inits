import csv


with open('/home/sampath/temp/FL_insurance_sample.csv/FL_insurance_sample.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
