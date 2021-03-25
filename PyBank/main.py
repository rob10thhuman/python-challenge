import os
import csv
import sys

# Tasks: 
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Lossese" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period


csvpath = os.path.join('Resources', '03-Python_HW_Instructions_PyBank_Resources_budget_data.csv')

balances = []
months = [] 

def average(numbers):
	length=len(numbers)
	total = 0.0
	for number in numbers:
		total += number 
	return round(total/length, 2)

with open(csvpath) as csvfile: 
	csvreader = csv.reader(csvfile, delimiter=',')
	print(csvreader)
	csv_header = next(csvreader)
	print(f"CSV Header: {csv_header}")
	total = 0
	lines = 0 
	nums = 0
	for row in csvreader:
		print(row[1])
		total += int(row[1])
		lines = lines + 1
		balances.append(int(row[1]))
		months.append(row[0])
	print(balances)
	print ("The original list is : " + str(balances)) 
	res = [balances[i + 1] - balances[i] for i in range(len(balances)-1)] 
	print ("The computed successive difference list is : " + str(res)) 
	resAvg = average(res)
	print(resAvg)
	print(max(res))
	index = res.index(max(res))+1
	indexMin = res.index(min(res))+1
	print(index)
	print(indexMin)
	maxMonth = months[index]
	minMonth = months[indexMin]

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(lines))
print("Total: " + str(total))
print("Average  Change: " + str(resAvg)) 
print("Greatest Increase in Profits: " + str(maxMonth)) 
print("Greatest Decrease in Profits: " + str(minMonth)) 

sys.stdout = open('log.txt', 'w')
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(lines))
print("Total: " + str(total))
print("Average  Change: " + str(resAvg)) 
print("Greatest Increase in Profits: " + str(maxMonth)) 
print("Greatest Decrease in Profits: " + str(minMonth)) 