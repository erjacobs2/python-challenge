import os
import csv

pollCSV = os.path.join("..", 'PyPoll', 'election_data.csv')

with open(pollCSV, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Line below skips header row
    next(csvreader, None)
    
#columns = Voter ID, County, Candidate

#Calculate total number of votes casted
    vote_count = list(csvreader)
    row_count = len(vote_count)
    print("Total Votes: " + str(len(vote_count)))

#Calculate complete list of candidates who received votes -- does NOT work, it prints all the names
#import csv
#import_candidate_list = csv.DictReader(open("election_data.csv"))
#unique_candidates = []
#def unique(list1):
#for row in import_candidate_list:
    #candidate_list = str(row["Candidate"])
    #if unique_candidates != candidate_list:
       #unique_candidates.append(candidate_list)
    #else: 
       #next
#if unique_candidates != 0:
    #print(unique_candidates)

#Calculate percentage of votes each candidate won -- does NOT work
#maybe use counter() to find the number of votes
#if running out of time tell it to count by name
import csv
from collections import Counter
import_list = csv.DictReader(open("election_data.csv"))
candidate_name = []
candidate_percent_list = []
candidate_total = []

for row in import_list:
    candidate1 = str(row["Candidate"])
    #votes = str(len(row["Candidate"]))
    if candidate_name != candidate1:
        candidate2 = str(row["Candidate"])
        candidate_name.append(candidate2)
        count = Counter(candidate2).items()
        candidate_total.append(count)
    else:
        candidate1 = 1
for i in candidate_total:
    i = round(((i/int(votes)) * 100), 2)
    candidate_percent_list.append(i) 
        #percentage = (int(count) / len(candidate_percent_list) * 100)
if candidate_percent_list != None:
    print("%s - %d%s %d") % (candidate_name, candidate_percent_list, "%", candidate_total)

#Calculate total number of votes each candidate won -- does NOT work yet
#do above minus the percentage calculation
#see min max script to see how it put the correlating name without making a seperate list
#import csv
#from collections import Counter
#import_votes_list = csv.DictReader(open("election_data.csv"))
#candidate_vote_list = []
#vote_list = None
#for row in import_votes_list:
    #candidate2 = str(row["Candidate"])
    #if canidate_vote_list not in candidate2:
        #candidate_vote_list.append(candidate2)
        #count = Counter(candidate_percent_list).items()
#if candidate_percent_list != 0:
    #print("%s - %d") % (candidate_percent_list, count)
        #add candidate name
        #add number of occurances of candidate name

#Calculate winner of election based on popular vote -- does NOT work yet
#import csv
#input_stuff = csv.DictReader(open("election_data.csv"))
#number_of_votes = []
#for row in input_stuff:
    #candidate = str(row["Candidate"])
    #need to loop through names while counting
    #need to print the name of the candidate with the most votes but don't print the number

#import csv
#input_file = csv.DictReader(open("budget_data.csv"))
#min_income = None
#date_min_income = None
#for row in input_file:
    #income2 = int(row["Profit/Losses"])
    #if min_income == None or min_income > income2:
        #min_income = income2
        #date_min_income = row["Date"]
#if min_income != None:
    #print(("The biggest decreaese in funds is $ %d in %s") % (min_income, date_min_income))
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

#from collection import Counter

#Below may help
#from collections import Counter
#names = ['adam','josh','drake']
#count = Counter(names).items()
#percentages = {x: int(float(y) / len(names) * 100) for x, y in count}
#for name, pct in percentages.iteritems():
    #print '%s - %s%s' % (name, pct, '%')