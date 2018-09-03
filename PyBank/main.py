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

        # loop through range 1 to number of items in list
   #for row in range(1, len(CSVlist)):

       #Total Revenue
       #revenue = revenue + int(CSVlist[row][1])
        
#list_of_values = 0
#total = 0
#row_number = 1
#for row in csvreader:
    #if row_number !=1
        #list_of_values = int(row[1])
        #total = total + list_of_values
        #print(total)
    #row_number += 1
#printer (total) 
#print (row_number)

#Averages between months - does not work  yet
import csv
input_funds = csv.DictReader(open("budget_data.csv"))
funds_total = None
difference_in_funds = None
for row in input_funds:
    funds = int(row["Profit/Losses"])
    numbering = len(funds)
    if funds_total == None
        #below will not work as is due to it subtracting everything
        funds_total -= funds + numbering
        average_difference =
        #count the number of subtractions that occur to divide later
        #use append, I think, to start to add each difference 
        break
    print("Average difference: $" + str(average_difference))

    #see month_count above to get number of months (number of rows)
    #tell it to subtract between each row in second [1] column
    #tell it to add the outputs from above
    #tell it to divide by the total number of outputs
    #previous = total
    #next

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

#the average change between each month for all of the data (single number output)
#first subtract between each month, and then take the average of all of those outputs

#create text file