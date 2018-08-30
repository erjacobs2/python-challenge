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
    
#Sum of Money -- does not work yet; no error but nothing prints
def Sum(money):
    for row in csvreader:
        list = [row[0], row[1]]
        moneylisted = list(1)
        #sumofmoney = []
        #totalmoney = []
        #for each entry in the money column (How do I say this?!)
        #I think the += is telling it to add... hopefully. 
        #for each x in range(moneylisted)
        #totalmoney.append(moneylisted[int(sum(money))])
        sumofmoney += int(moneylisted)
        print("Total: $" + sum(sumofmoneyy))
        #print(f"Total: $ + {float(sumofmoney)}")
        #need to figure out how to tell it sum of column 2 (actually 1). 
        #I think it would be row[1] something. Maybe.
        #can I tell the computer[row, column]?
        #Do I need to redo the with open(budgetCSV....) for each time? 

#Averages Between Months -- does not work yet
#def Averages(betweenmonths):
    #for row in csv reader:
        # months = (month[0])
        # monthmoney = (monthmoneys[1])
        #for each monthmoney in months
        # return monthmoney(first) - monthmoney(second)
    #tell it to subtract between each row in second [1] column
    #tell it to add the outputs from above
    #tell it to divide by the total number of outputs

#Date and Profit/Losses columns 
#Date is Month and Year, column 0
#Profit and loses have no decimals, commas or dollar signs; column 1

#sum of numbers in Profit/losses columns

#the average change between each month for all of the data (single number output)
#first subtract between each month, and then take the average of all of those outputs

#find the biggest increase in funds in data by date and amount

#find the biggest decrease in losses in data by date and amount

#print terminal

#create text file