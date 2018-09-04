import os
import csv

pollCSV = os.path.join("..", 'PyPoll', 'election_data.csv')

with open(pollCSV, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Line below skips header row
    next(csvreader, None)
    
#columns = Voter ID, County, Candidate

#Calculate total number of votes casted -- should work? I need to re-test with other code working or turned off
    vote_count = list(csvreader)
    row_count = len(vote_count)
    print("Total Votes: " + str(len(vote_count)))

#Calculate complete list of candidates who received votes -- should work but has NOT been tested yet
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

#Calculate percentage of votes each candidate won -- does NOT work yet
#maybe use counter() to find the number of votes
import csv
from collections import Counter
import_percent_list = csv.DictReader(open("election_data.csv"))
candidate_percent_list = None
#vote_percent_list = None <== may need another empty list so that candidate names are listed separately from their percentages
for row in import_percent_list:
    candidate1 = str(row["Candidate"])
    if candidate_percent_list not in candidate1:
        #may need to move counter statement below somewhere else
        candidate_percent_list.append(candidate1)
        count = Counter(candidate_percent_list).items()
        percentage = {x: int(float(y) / len(candidate_percent_list) * 100) for x, y in count}
if candidate_percent_list != None:
    print(%s - %s%s) % (candidate_percent_list, percentage, "%")
        #need to both name and count candidates, the above I think only counts them but may name them too
        #need to calculate the number of candidate votes divide by total number of votes and multiply by 100

#Below may help
#from collections import Counter
#names = ['adam','josh','drake']
#count = Counter(names).items()
#percentages = {x: int(float(y) / len(names) * 100) for x, y in count}
#for name, pct in percentages.iteritems():
    #print '%s - %s%s' % (name, pct, '%')

#Calculate total number of votes each candidate won -- does NOT work yet
#do above minus the percentage calculation
import csv
from collections import Counter
import_votes_list = csv.DictReader(open("election_data.csv"))
candidate_vote_list = None
vote_list = None
for row in import_votes_list:
    candidate2 = str(row["Candidate"])
    if canidate_vote_list not in candidate2:
        candidate_vote_list.append(candidate2)
        count = Counter(candidate_percent_list).items()
if candidate_percent_list != None:
    print(%s - %s) % (candidate_percent_list, count)
        #add candidate name
        #add number of occurances of candidate name

#Calculate winner of election based on popular vote -- does NOT work yet
import csv
input_stuff = csv.DictReader(open("election_data.csv"))
number_of_votes = None
for row in input_stuff:
    candidate = str(row["Candidate"])
    #need to loop through names while counting
    #need to print the name of the candidate with the most votes but don't print the number

    #if max_income == None or max_income < income:
        #max_income = income
        #date_max_income = row["Date"]
#if max_income != None:
    #print(("The biggest increase in funds is $ %d in %s") % (max_income, date_max_income))
#else:
    #print("Uh oh!")

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