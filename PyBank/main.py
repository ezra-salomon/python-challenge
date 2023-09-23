#import os module csv file to read from
import os
import csv

#constants
totalMonths = 1
totalProf = 0
totalChange = 0
chgAve = 0
dateGreat = " "
dateMin = " "
greatProf = 0
greatLoss = 0


#working code
csvpath = os.path.join('/Users/ezrasalomon/Desktop/Bootcamp/Python/python-challenge/PyBank', 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)
    header = next(csvreader)
    sec_row = next(csvreader)
    prev_row = next(csvreader)
    totalMonths += 1
    totalProf += int(prev_row[1])
    totalProf += int(sec_row[1])
    totalChange += int(prev_row[1]) - int(sec_row[1])
    greatProf += int(prev_row[1]) - int(sec_row[1])
    greatLoss += int(prev_row[1]) - int(sec_row[1])
    dateGreat = prev_row[0]
    dateMin = prev_row[0]

    for row in csvreader:
        totalMonths += 1
        totalProf += int(row[1])
        totalChange += int(row[1]) - int(prev_row[1])
        

        if int(row[1]) - int(prev_row[1]) > greatProf:
            greatProf = int(row[1]) - int(prev_row[1])
            dateGreat = row[0]

        if int(row[1]) - int(prev_row[1]) < greatLoss:
            greatLoss = int(row[1]) - int(prev_row[1])
            dateMin = row[0]
            



        prev_row = row
        
chgAve = totalChange / (totalMonths - 1)
         
        
#output
print("Financial Analysis")
print(f"Total Months: {totalMonths} ")
print(f"Total: ${totalProf}")
print(f"Total Change: ${chgAve}")
print(f"Greatest Increase in Profits:{dateGreat}({greatProf})")
print(f"Greatest Loss in Profits:{dateMin}({greatLoss})")




