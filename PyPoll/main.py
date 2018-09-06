import os
import csv

pollCSV = os.path.join("..", 'PyPoll', 'election_data.csv')

with open(pollCSV, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Line below skips header row
    next(csvreader, None)

#Calculate total number of votes casted
    vote_count = list(csvreader)
    row_count = len(vote_count)
    print("Total Votes: " + str(len(vote_count)))

#Below does not work
with open(pollCSV, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    names = []
    vote_count = list(csvreader)
    row_count = len(vote_count)
    for row in csvreader:
        names.append(row[2])
    print(names)

#calculate the votes per candidate and the percentage - does not work
import csv
from collections import Counter
input_file = csv.DictReader(open("election_data.csv"))
percent = []
total = []
for row in input_file:
    candidates = row["Candidate"]
    count = Counter(candidates).items()
    total.append(count)
for i in total:
    percentage = (int(count) / len(candidate_percent_list) * 100)
if total != None:
    print("%s - %d%s %d") % (candidates, percent, "%", total)


#Calculate winner of election based on popular vote -- does NOT work yet
#import csv
#input_stuff = csv.DictReader(open("election_data.csv"))
#number_of_votes = []
#for row in input_stuff:
    #candidate = str(row["Candidate"])
    #need to loop through names while counting
    #need to print the name of the candidate with the most votes but don't print the number

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