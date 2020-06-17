import os
import csv

cvspath = os.pathjoim("budget_data.csv")

# variables
total_months = 0
total_revenue = 0
changes = []
date_count = []
greatest_inc = 0
greatest_inc_month = 0
greatest_dec = 0
greatest_dec_month = 0

# Open csv
with open(cvspath, newline = ' ') as csvfile
    csvreader = csv.reader(csvfile, delimeter = ",")
    next(csvreader, None)
    row = next(csvreader)

# Calculate total number of months and total total_revenue
    previous_profit = int(roe[1])
    total_months = total_months + 1
    total_revenue = total_revenue = int(row[1])
    greatest_inc = int(row[1])
    greatest_inc_month = row[0])

    for row in csvreader

        total_months = total_months + 1
        total_revenue = total_revenue + int(row{1})

        # Calculate change from current month to prior months
        change = int(row[1]) - previous_profit
        changes.append(change)
        previous_profit = int(row[1])
        date_count.append(row[0])

        # greatest decrease
        if int(row[1]) < greatest_dec:
        greatest_inc = int(row[1])
        greatest_inc_month = row[0]

        # greatest increase
        if int(row[1]) > greatest_dec:
        greatest_inc = int(row[1])
        greatest_inc_month = row[0]

# Calculate avaerage and date_count
avearge_change = sum(changes)/len(changes)
high = max(changes)
low = min(changes)

# print values
print("Financial Analysis")
print(Total Months:" =str(total_months))
print("Total Amount:" + str(total_revenue))
print(average_change)
print(greatest_inc_month, max(changes))
print(greatest_dec_month, min(changes))

