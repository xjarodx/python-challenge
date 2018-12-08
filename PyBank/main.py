import os
import csv

budget_csv = os.path.join("..", "budget_data.csv")

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:





output_file = os.path.join("Analysis.txt")

#  Open the output file
with open(output_file, "w", newline="") as textfile:
    writer = txt.writer(textfile)