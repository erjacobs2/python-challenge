#budget_data.csv
#calculate:
#total number of months included in dataset
#total net amount of "profit/losses" over the entire period
#average change in proft/loses between months over entire period
#greatest increase in profits (date and amount) over the entire period
#the greatest decrease in losses (date and amount) over the entire period
#results should print in terminal and export a text file with results
#see instructions for how output should look

import os
import csv

budgetCSV = os.path.join("..", 'PyBank', 'budget_data.csv')

#what does the thing after the comma do? What's the difference between newline="" and r?
with open(budgetCSV, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Line below skips header row
    next(csvreader, None)

#Total number of months
    months_count= list(csvreader)
    row_count = len(months_count)
    print("Total Months: " + str(len(months_count)))

#Sum of Money
with open(budgetCSV, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    total = 0
    for row in csvreader: 
        sumofmoney = int(row[1])
        total = total + sumofmoney
    print("Total: $" + str(total))

#Averages between months - works, but output number does not match what's listed on GitLab

with open(budgetCSV, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    difference_in_funds = []
    months_count= list(csvreader)
    row_count = len(months_count)
    for row in range(1, len(months_count)-1): 
        first = int(months_count[row][1])
        second = int(months_count[row+1][1])
        difference = second - first
        difference_in_funds.append(difference)
average_differences = round(sum(difference_in_funds)/(row_count-1), 2)
print("The average difference between months is $" + str(average_differences))

#Averages between months with dictionary - does not work
#import csv
#input_funds = csv.DictReader(open("budget_data.csv"))
#difference_in_funds = 0
#for row in input_funds:
    #first = int(row["Profit/Losses"])
    #second = int(row["Profit/Losses" + 1])
    #difference = second-first
    #difference_in_funds.append(difference)
#average_differences = round(sum(difference_in_funds)/(months_count-1), 2)

#Biggest increase by date and amount
import csv
input_stuff = csv.DictReader(open("budget_data.csv"))
max_income = None
date_max_income = None
for row in input_stuff:
    income = int(row["Profit/Losses"])
    if max_income == None or max_income < income:
        max_income = income
        date_max_income = row["Date"]
if max_income != None:
    print(("The biggest increase in funds is $ %d in %s") % (max_income, date_max_income))
else:
    print("Uh oh!")

#Biggest decreae by date and amount
import csv
input_file = csv.DictReader(open("budget_data.csv"))
min_income = None
date_min_income = None
for row in input_file:
    income2 = int(row["Profit/Losses"])
    if min_income == None or min_income > income2:
        min_income = income2
        date_min_income = row["Date"]
if min_income != None:
    print(("The biggest decreaese in funds is $ %d in %s") % (min_income, date_min_income))
else:
    print("Uh oh!") 

#create text file - see below for similar example
# Dependencies
#import os
#import csv

# Specify the file to write to
#output_path = os.path.join("..", "output", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
#with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    #csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    #csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

    # Write the second row
    #csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])
