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
#it may not like that statement below is not tabbed/does not have new csv open

def unique(list1):
    unique_candidates = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_candidates:
        print(x)

#Calculate percentage of votes each candidate won
#maybe use counter() to find the number of votes
import csv
import_list = csv.DictReader(open("election_data.csv"))

#def getPercentages(polldata):
    #percentagewon = (int(polldata[2])/row_count) * 100
    #for row in csvreader:
        #below works when there is an input - I don't know if it will find when there's no input
        #below won't work since candidate name isn't defined
        #if(candidatename == row[0])
            #getPercentages(row)

#Calculate total number of votes each candidate won
#will need a way to find unique names and count each time a name appears

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