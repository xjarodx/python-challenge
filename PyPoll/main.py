import os
import csv
from collections import Counter

election_data = os.path.join("../PyPoll", "election_data.csv")

with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None) 
    
    # Creates a list from the csv file
    data=list(csvreader)

    # Counts row
    row_count = len(data)

    # Creates a dictionary to hold canidate vote counts
    canidates = {}
    
    canidates["Khan"]=0
    canidates["Correy"]=0
    canidates["Li"]=0
    canidates["O'Tooley"]=0
    
    # Gets number of votes per canidate and sends them to Canidates dictionary
    for row in data:
        
        if row[2] == "Khan":
            canidates["Khan"]+=1
        elif row[2] == "Correy":
            canidates["Correy"]+=1
        elif row[2] == "Li":
            canidates["Li"]+=1
        elif row[2] == "O'Tooley":
            canidates["O'Tooley"]+=1

    # Converts the vote counts in the Canidates dictionary into percentages of total votes
    
    Khan_percent = canidates["Khan"] / row_count *100
    toprintkhanpercent = str(Khan_percent)#turns it into a string
    Khan_votes = str(canidates["Khan"])#turns it into a string
    
    Correy_percent = canidates["Correy"] / row_count *100
    toprintCorreypercent = str(Correy_percent)
    Correy_votes = str(canidates["Correy"])

    Li_percent = canidates["Li"] / row_count *100
    toprintLipercent = str(Li_percent)
    Li_votes = str(canidates["Li"])
    
    OTooley_percent = canidates["O'Tooley"] / row_count *100
    toprintOTooleypercent = str(OTooley_percent)
    OTooley_votes = str(canidates["O'Tooley"])

    #Returns the Key in the Canidates dictionary with the largest Value
    Winner = max(canidates, key=lambda x: canidates[x]) 
    
    
print ("Election Results")
print ("-------------------------------")
print ("Total Votes: ", row_count)
print ("-------------------------------")
print ("Khan: ", "{:.2f}".format(Khan_percent), "% ", canidates["Khan"])    # Could not get these to print to text file in next section. Error code below:
print ("Correy: ", "{:.2f}".format(Correy_percent), "% ", canidates["Correy"])       # text_file.write (f"Khan: "+ str("{:.2f}".format(Khan_percent))+ "% "+ 
print ("Li: ", "{:.2f}".format(Li_percent), "% ", canidates["Li"])                      # canidates["Khan"] + "\n") TypeError: can only concatenate str (not "int") to str
print ("O'Tooley: ", "{:.2f}".format(OTooley_percent), "% ", canidates["O'Tooley"])
print ("-------------------------------")
print ("Winner: ", Winner)
print ("-------------------------------")


output_file = os.path.join("Election Analysis.txt")

#  Open the output file
with open(output_file, "w") as text_file:
    text_file.write (f"Election Results\n")
    text_file.write (f"-------------------------------\n")
    text_file.write (f"Total Votes: " + str(row_count) + "\n")
    text_file.write (f"-------------------------------\n")
    text_file.write (f"Khan: "+ str(toprintkhanpercent) + "% "+ str(Khan_votes) + "\n")
    text_file.write (f"Correy: "+ str(toprintCorreypercent) + "% "+ str(Correy_votes) + "\n")
    text_file.write (f"Li: "+ str(toprintLipercent) + "% "+ str(Li_votes) + "\n")
    text_file.write (f"O'Tooley: "+ str(toprintOTooleypercent) + "% "+ str(OTooley_votes) + "\n")
    text_file.write (f"-------------------------------\n")
    text_file.write (f"Winner: " + Winner + "\n")     
    text_file.write (f"-------------------------------") 