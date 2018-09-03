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

import csv
import_candidate_list = csv.DictReader(open("election_data.csv"))
unique_candidates = None
#def unique(list1):
for row in import_candidate_list:
    candidate_list = str(row["Candidate"])
    if unique_candidates not in candidate_list:
       unique_candidates.append(candidate_list)
if unique_candidates != None:
    print(unique_candidates)

#Calculate percentage of votes each candidate won
#maybe use counter() to find the number of votes
import csv
import_percent_list = csv.DictReader(open("election_data.csv"))
candidate_percent_list = None
vote_percent_list = None
for row in import_percent_list:
    candidate1 = str(row["Candidate"])
    if candidate_percent_list not in candidate1:
        #need to pull the candidates
        #need to calculate the number of candidate votes divide by total number of votes and multiply by 100

#Below may help
#from collections import Counter
#names = ['adam','josh','drake']
#count = Counter(names).items()
#percentages = {x: int(float(y) / len(names) * 100) for x, y in count}
#for name, pct in percentages.iteritems():
    #print '%s - %s%s' % (name, pct, '%')

#Calculate total number of votes each candidate won
#do above minus the percentage calculation

#Calculate winner of election based on popular vote
import csv
input_stuff = csv.DictReader(open("election_data.csv"))
number_of_votes = None
for row in input_stuff:
    candidate = str(row["Candidate"])
    #if max_income == None or max_income < income:
        #max_income = income
        #date_max_income = row["Date"]
#if max_income != None:
    #print(("The biggest increase in funds is $ %d in %s") % (max_income, date_max_income))
#else:
    #print("Uh oh!")