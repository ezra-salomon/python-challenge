#import os module csv file to read from
import os
import csv

#constants
totalMonths = 0
totalProf = 0
aveChange = totalProf % 86
#greatProf = 0


#working code
csvpath = os.path.join('/Users/ezrasalomon/Desktop/Bootcamp/Python/python-challenge/PyBank', 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    
    header = next(csvreader)
    for row in csvreader:
        totalMonths += 1
        totalProf += int(row[1])
        #aveChange totalProf % 86

        #greatProf += max(int(row[1]))

        #print(int(row[1]))
        #row[0] += str(totalMonths)
#output
print("Financial Analysis")
print(f"Total Months: {totalMonths} ")
print(f"Total: ${totalProf}")
print(f"Average Change: ${aveChange}")
#print(f"Greatest Increase in Profits: {greatProf}")





