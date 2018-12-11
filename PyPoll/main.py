import os
import csv
from collections import Counter

election_data = os.path.join("../PyPoll", "election_data.csv")

with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header row
    next(csvreader, None) 
    
    # Gets number of rows in csv
    data=list(csvreader)

    row_count = len(data)
    
    #gets count of votes each canidate recieved
    #canidate = []
    #for row in data:
    #    name = row[2]
    #    canidate.append(name)
    #canidate_count = Counter(canidate)
    #print (canidate_count)

    canidates = {}
    for row in data:
        if not row[2] in canidates:
            canidates[row[2]] = 0
        if row[2] == "Khan":
            canidates["Khan"]+=1
        elif row[2] == "Correy":
            canidates["Correy"]+=1
        elif row[2] == "Li":
            canidates["Li"]+=1
        else row[2] == "O'Tooley":
            canidates["O'Tooley"]+=1

    
    
    #print(canidates["Khan"])
    print (canidates)


    #Khan = []
   # for row in data:
    #    where row[2] == "Khan" is True
     #   Khan.append()

    #print (Khan)
    
print ("Election Results")
print ("-------------------------------")
print ("Total Votes: ", row_count)
print ("-------------------------------")
#print ("Total: ", '${:,.2f}'.format(totals3))
#print ("Average Change: ", '${:,.2f}'.format(average))
#print ("Greatest Increase in Profits: ", '${:,.2f}'.format(greatest))
#print ("Greatest Decrease in Profits: ", '${:,.2f}'.format(smallest))



output_file = os.path.join("Election Analysis.txt")

#  Open the output file
with open(output_file, "w") as text_file:
    text_file.write (f"Election Results\n")
    text_file.write (f"-------------------------------\n")
    text_file.write (f"Total Votes: " + str(row_count) + "\n")
    text_file.write (f"-------------------------------\n")
    #text_file.write (f"Total: " + '${:,.2f}'.format(totals3) + "\n")
    #text_file.write (f"Average Change: " + '${:,.2f}'.format(average) + "\n")
    #text_file.write (f"Greatest Increase in Profits: " + '${:,.2f}'.format(greatest) + "\n")
    #text_file.write (f"Greatest Decrease in Profits: "+ '${:,.2f}'.format(smallest) + "\n")    