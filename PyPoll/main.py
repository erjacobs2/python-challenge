import os
import csv

pollCSV = os.path.join("..", 'PyPoll', 'election_data.csv')

with open(pollCSV, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Line below skips header row
    next(csvreader, None)
    
#import election_data.csv
#columns = Voter ID, County, Canidate

#Calculate total number of votes casted
    vote_count = list(csvreader)
    row_count = len(vote_count)
    print("Total Votes: " + str(len(vote_count)))

#Calculate complete list of candidates who received votes

#Calculate percentage of votes each candidate won
#How do I tell it to do it for each individual canidate? 
#def getPercentages(polldata):
    #percentagewon = (int(polldata[2])/row_count) * 100
    #for row in csvreader:
        #below works when there is an input - I don't know if it will find when there's no input
        #below won't work since candidate name isn't defined
        #if(candidatename == row[0])
            #getPercentages(row)

#Calculate total number of votes each candidate won

#Calculate winner of election based on popular vote
import csv
input_stuff = csv.DictReader(open("election_data.csv"))
number_of_votes = None
for row in input_stuff:
    candidate = str(row["Candidate"])
    if max_income == None or max_income < income:
        max_income = income
        date_max_income = row["Date"]
if max_income != None:
    print(("The biggest increase in funds is $ %d in %s") % (max_income, date_max_income))
else:
    print("Uh oh!")