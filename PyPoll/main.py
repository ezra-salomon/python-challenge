#import os module csv file to read from
import os
import csv

#variable assignments
totalVotes = 0
ccs = "Charles Casper Stockham"
ccsVts = 0
ddg = "Diana DeGette"
ddgVts = 0
rad = "Raymon Anthony Doane"
radVts = 0 
winner = " "
percVtsC = 0
percVtsD = 0
percVtsR = 0

csvpath = os.path.join('/Users/ezrasalomon/Desktop/Bootcamp/Python/python-challenge/PyPoll', 'Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    


#iterate through csv file
    for row in csvreader:
        totalVotes += 1

        
#determin number and percentage of votes for each candidates
        if row[2] == ccs:
            ccsVts += 1
            percVtsC = (ccsVts / totalVotes * 100)
        elif row[2] == ddg:
            ddgVts += 1
            percVtsD = (ddgVts / totalVotes * 100)
        else: radVts += 1
        percVtsR = (radVts / totalVotes * 100)
#Determine winner
        if ccsVts > ddgVts + radVts:
            winner = ccsVts
        elif ddgVts > ccsVts + radVts:
            winner = ddg
        elif radVts > ccsVts + ddgVts:
            winner = radVts
        
        




        

print("Election Results")
print(f"Total votes:{totalVotes}")
print(f"Charles Casper Stockham:{percVtsC}% ({ccsVts})")
print(f"Diana DeGette:{percVtsD}% ({ddgVts})")
print(f"Raymon Anthony Doane:{percVtsR}% ({radVts})")
print(f"Winner: {winner}")
