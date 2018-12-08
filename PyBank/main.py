import os
import csv

budget_csv = os.path.join("../PyBank", "budget_data.csv")

#def get_months():
#    months=len(list(reader -1))


dict_list = []


with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #reader = csv.DictReader(open(budget_csv, 'rb'))
    
    for line in csvreader:
        dict_list.append(line)






output_file = os.path.join("Analysis.txt")

#  Open the output file
with open(output_file, "w", newline="") as textfile:
    writer = textfile.writer(dict_list)