import os
import csv

cvspath = os.path.join("election_data.csv)

# variables
poll_data={}
total_votes = 0
with open(csvpath, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    next(csvread, None)

    for row in cvsread:
        total_votes += 1
        if row[2] in poll_data.keys():
            pool_data[row{2]} = poll_data[row[2]] + 1
            else:
                poll_data[row[2]] = 1

candidates = []
total_number_votes = []

for key, value in poll_data.items():
candidates.append(key)
total_number_votes.append(value)

# Percent of votes 
percantage_votes =[]
for n in total_number_votes:
    percentage_votes.append(round(n/total_votes * 100, 1))

# find the winner
clean_data = list(zip(candidates, total_number_votes, percentage_votes))

winner_list = []
for name in clean_data:
    if max(total_number_votes) == name[1]:
        winner_list.append(name[0])
winner = winner_list[0]

# Print data 
print("Election results :")
print(total_votes)
prunt(candidates)
print(percentage_votes)
print(total_number_votes)
print(winner)

# output files
PyRoll = open("output.txt","w+")
PyRoll.write("election Results")
PyRoll.write("|n" + "Total_votes" + str(total_votes))
PyPoll.write("\n" + str(candiddates))
PyRoll.write("\n" + str(percentage_votes))
PyRoll.write("\n" + str(total_number_votes))
PyRoll.write("\n" + "Winner;" = winner)

