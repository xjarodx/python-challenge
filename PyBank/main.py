import os
import csv

budget_csv = os.path.join("../PyBank", "budget_data.csv")

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header row
    next(csvreader, None) 
    
    # Gets number of rows in csv
    data=list(csvreader)
    
    row_count = len(data)

    #Sets initial value of the net sum
    net = 0

    #gets values from rows
    for row in csvreader:
        net += float(row[1])





print ("Financial Analysis")
print ("-------------------------------")
print ("Total Months: ", row_count)
print ("Total: {}".format(net))
print ("Average Change: ")
print ("Greatest Increase in Profits: ")
print ("Greatest Decrease in Profits: ")



output_file = os.path.join("Analysis.txt")

#  Open the output file
with open(output_file, "w") as text_file:
    text_file.write (f"Financial Analysis")
    text_file.write (f"-------------------------------")
    text_file.write (f"Total Months: ", row_count)
    #print (f"Total: {}".format(net))
    #print (f"Average Change: ")
    #print (f"Greatest Increase in Profits: ")
    #print (f"Greatest Decrease in Profits: ")    