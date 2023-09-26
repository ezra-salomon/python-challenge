#import os module csv file to read from
import os
import csv
 

#Define variables 
totalMonths = 1
totalProf = 0
totalChange = 0
chgAve = 0
dateGreat = " "
dateMin = " "
greatProf = 0
greatLoss = 0



#working code
#csvpath = os.path.join('/Users/ezrasalomon/Desktop/Bootcamp/Python/python-challenge/PyBank', 'Resources', 'budget_data.csv')
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#access csv reader and update variables 
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
#Initalize for loop to iterate through csv file 
    for row in csvreader:
#Find the total number of months in csv file, net profit, and total change in profits
        totalMonths += 1
        totalProf += int(row[1])
        totalChange += int(row[1]) - int(prev_row[1])
        
#Find greatest increase in profits and their percentage
        if int(row[1]) - int(prev_row[1]) > greatProf:
            greatProf = int(row[1]) - int(prev_row[1])
            dateGreat = row[0]
#Find the greatest decrease in profits and their percentage
        if int(row[1]) - int(prev_row[1]) < greatLoss:
            greatLoss = int(row[1]) - int(prev_row[1])
            dateMin = row[0]
#Reassigne row
        prev_row = row
#calculate average change        
chgAve = totalChange / (totalMonths - 1)
         
        
#output
lines = f"""Financial Analysis
Total Months: {totalMonths}
Total: ${totalProf}
Total Change: ${chgAve}
Greatest Increase in Profits:{dateGreat}({greatProf})
Greatest Loss in Profits:{dateMin}({greatLoss})
"""
print(lines)



#with open('/Users/ezrasalomon/Desktop/Bootcamp/Python/python-challenge/PyBank/analysis/analysis.txt', 'w') as file:
with open('analysis/analysis.txt', 'w') as f:
    f.write(lines)

    
    


