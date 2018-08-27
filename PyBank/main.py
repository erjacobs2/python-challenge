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

with open(budgetCSV, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    #Total number of months
    months= list(csvreader)
    row_count = len(months)
    print("Total Months: " + str(len(months)))

#define variables, determine if lists or dictionaries would help
#determine loops or functions that will allow for calculations
#instruct to both print in terminal and to create text file

#Date and Profit/Losses columns 
#Date is Month and Year, column 0
#Profit and loses have no decimals, commas or dollar signs; column 1

#function to count the total number of months in data
# to skip first row/header: next(csv_reader, None)
#take information from column 1, before the -

#sum of numbers in Profit/losses columns

#the average change between each month for all of the data (single number output)

#find the biggest increase in funds in data by date and amount

#find the biggest decrease in losses in data by date and amount

#print terminal

#create text file