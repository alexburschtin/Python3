import os
import csv

    
# PyPoll_csv = os.path.join('..', '..', '..', '..', 'columbia', 'myWork', 'homework', '03-Python', 'Instructions', 'PyPoll', 'Resources', 'election_data.csv')
PyPoll_csv = os.path.join('Resources', 'election_data.csv')
count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []


with open(PyPoll_csv, 'r') as Poll_data:
    csvreader = csv.reader(Poll_data, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:

        count = count + 1

        candidatelist.append(row[2])
    
    for x in set(candidatelist):
        unique_candidate.append(x)

        y = candidatelist.count(x)
        vote_count.append(y)

        z = (y/count)*100
        vote_percent.append(z)
        
        winning_vote_count = max(vote_count)
        winner = unique_candidate[vote_count.index(winning_vote_count)]

print("-------------------------")
print("Election Results")
print("-------------------------")
print("Total Votes :" + str(count))
print("-------------------------")
for i in range(len(unique_candidate)):
    print(unique_candidate[i] + ": " + str(round(vote_percent[i],4)) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(round(vote_percent[i],4)) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")