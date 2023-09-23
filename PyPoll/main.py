#import os module csv file to read from
import os
import csv

totalVotes = 0
ccs = "Charles Casper Stockham"
ccsVts = 0
ddg = "Diana DeGette"
ddgVts = 0
rad = "Raymon Anthony Doane"
radVts = 0 
winner = " "

csvpath = os.path.join('/Users/ezrasalomon/Desktop/Bootcamp/Python/python-challenge/PyPoll', 'Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    #ccsNumVts = next(csvreader)
    #nameCount = next(csvreader)



    for row in csvreader:
        totalVotes += 1

        #ccsVts += row[2]

        if row[2] == ccs:
            ccsVts += 1
        elif row[2] == ddg:
            ddgVts += 1
        else: radVts += 1

        if ccsVts > ddgVts + radVts:
            winner = ccsVts
        elif ddgVts > ccsVts + radVts:
            winner = ddg
        elif radVts > ccsVts + ddgVts:
            winner = radVts
        
        #if nameCount(str(row[2])).count(nameCount):




        

print("Election Results")
print(f"Total votes:{totalVotes}")
print(f"Charles Casper Stockham:({ccsVts})")
print(f"Diana DeGette:({ddgVts})")
print(f"Raymon Anthony Doane:({radVts})")
print(f"Winner:{winner}")
