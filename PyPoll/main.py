import os
import csv
import sys

# Tasks: 
# The total number of votes cast
#	DONE: This is essentially counting the lines 
# A complete list of candidates who received votes
#	DONE: Need to identify the unique candidates 
# The percentage of votes each candidate won
#	DONE: Need to count the votes each recieved the divide by the total
# The total number of votes each candidate won
#	DONE as a function of the above
# The winner of the election based on popular vote.
#	DONE


csvpath = os.path.join('Resources', '03-Python_HW_Instructions_PyPoll_Resources_election_data.csv')

unique = []
test = []
tallies = []
votes0 = 0
votes1 = 0
votes2 = 0
votes3 = 0

v0p = 0
v1p = 0
v2p = 0
v3p = 0

with open(csvpath) as csvfile: 
	csvreader = csv.reader(csvfile, delimiter=',')
	print(csvreader)
	csv_header = next(csvreader)
	print(f"CSV Header: {csv_header}")

	lines = 0 
	can1 = 0
	
	for row in csvreader:
		lines = lines + 1
		if row[2] not in unique:
			unique.append(row[2])
		test.append(row[2])

	votes0 = test.count(unique[0])
	votes1 = test.count(unique[1])
	votes2 = test.count(unique[2])
	votes3 = test.count(unique[3])
	tallies = {unique[0]: votes0, 
				unique[1]: votes1, 
				unique[2]: votes2, 
				unique[3]: votes3}

	v0p = round((votes0 / lines) * 100, 3)
	v1p = round((votes1 / lines) * 100, 3)
	v2p = round((votes2 / lines) * 100, 3)
	v3p = round((votes3 / lines) * 100, 3)

winner = max(tallies, key=tallies.get)

print(winner)
print(v0p)
print(v1p)
print(v2p)
print(v3p)
print(unique)
print(lines)

sys.stdout = open('log.txt', 'w')
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(lines))
print("----------------------------")
print("Khan: " + str(v0p) + "%" + "(" + str(votes0) + ")")
print("Correy: " + str(v1p) + "%" + "(" + str(votes1) + ")")
print("Li: " + str(v2p) + "%" + "(" + str(votes2) + ")")
print("O'Tooley: " + str(v3p) + "%" + "(" + str(votes3) + ")")
print("----------------------------")
print("Winner: " + winner)
print("----------------------------")


