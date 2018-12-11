import os
import csv
import statistics
import numpy

budget_csv = os.path.join("../PyBank", "budget_data.csv")

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header row
    next(csvreader, None) 
    
    # Gets number of rows in csv
    data=list(csvreader)

    row_count = len(data)
    
    #creates initial list of values in csv as integers
    totals1 = []
    for row in data:
        values = row[1]
        totals1.append(values)

    #turns values in totals1 into floats
    totals2 = [float(integral) for integral in totals1]
    
    #sets totals2 equal to printable variable
    totals3 = sum(totals2)
    
    #gets differences between list items
    difference = numpy.diff(totals2)

    #largest and smallest differences
    average = statistics.mean(difference)
    greatest = max(difference)
    smallest =min(difference)


print ("Financial Analysis")
print ("-------------------------------")
print ("Total Months: ", row_count)
print ("Total: ", '${:,.2f}'.format(totals3))
print ("Average Change: ", '${:,.2f}'.format(average))
print ("Greatest Increase in Profits: ", '${:,.2f}'.format(greatest))
print ("Greatest Decrease in Profits: ", '${:,.2f}'.format(smallest))



output_file = os.path.join("Analysis.txt")

#  Open the output file
with open(output_file, "w") as text_file:
    text_file.write (f"Financial Analysis\n")
    text_file.write (f"-------------------------------\n")
    text_file.write (f"Total Months: " + str(row_count) + "\n")
    text_file.write (f"Total: " + '${:,.2f}'.format(totals3) + "\n")
    text_file.write (f"Average Change: " + '${:,.2f}'.format(average) + "\n")
    text_file.write (f"Greatest Increase in Profits: " + '${:,.2f}'.format(greatest) + "\n")
    text_file.write (f"Greatest Decrease in Profits: "+ '${:,.2f}'.format(smallest) + "\n")    