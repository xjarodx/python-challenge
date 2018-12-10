import os
import csv

budget_csv = os.path.join("../PyBank", "budget_data.csv")

#def average(numbers):
#    length = len(csvreader)
#    total = 0.0
#    for number[1] in numbers:
#        total += number
#    return total / length


with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header row
    next(csvreader, None) 
    
    # Gets number of rows in csv
    data=list(csvreader)

    row_count = len(data)
    
    #B = {rows[0]:rows[1] for rows in csvreader}
    #print (sum(B.values()))
    totals = []
    for row in csvreader:
        values = row[1]
        totals.append(values)

    print (totals)



print ("Financial Analysis")
print ("-------------------------------")
print ("Total Months: ", row_count)
print ("Total: ", sum(totals))
print ("Average Change: ")
print ("Greatest Increase in Profits: ")
print ("Greatest Decrease in Profits: ")



output_file = os.path.join("Analysis.txt")

#  Open the output file
with open(output_file, "w") as text_file:
    text_file.write (f"Financial Analysis\n")
    text_file.write (f"-------------------------------\n")
    text_file.write (f"Total Months: " + str(row_count) + "\n")
    #print (f"Total: {}".format(net))
    #print (f"Average Change: ")
    #print (f"Greatest Increase in Profits: ")
    #print (f"Greatest Decrease in Profits: ")    