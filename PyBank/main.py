import os
import csv

budget_csv = os.path.join("../PyBank", "budget_data.csv")

#def get_months():
#    months=len(list(reader -1))

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    month_total = len(list(cvsreader -1))
    print(month_total)


output_file = os.path.join("Analysis.txt")

#  Open the output file
with open(output_file, "w", newline="") as textfile:
    writer = txt.writer(textfile)