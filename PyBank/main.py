import os
import csv

budget_csv = os.path.join('Resources', 'budget_data.csv')

#budget_csv = os.path.join('..', '..', '..', '..', 'columbia', 'myWork', 'homework', '03-Python', 'Instructions', 'PyBank', 'Resources', 'budget_data.csv')


with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip header.
    next(csvreader)

    # Variables to calculate.
    num_months = 0
    total_amount = 0
    total_delta = 0
    max_delta = 0
    min_delta = 0
    max_month = 'month'
    min_month = 'month'

    last_row_value = None

    # Loop through the data
    for row in csvreader:

        if last_row_value is None:
            last_row_value = int(row[1])

        delta = int(row[1]) - last_row_value 
        total_delta = total_delta + delta 

        num_months = num_months + 1
        total_amount = total_amount + int(row[1])

        max_delta = max(max_delta, delta)
        if delta == max_delta:
            max_month = row[0]

        min_delta = min(min_delta, delta)
        if delta == min_delta:
            min_month = row[0]

    # Loop end
    print("Financial Analysis")
    print("-----------------------")
    print(f"Total Months: {num_months}")
    print(f"Total: ${total_amount}")
    print("Average change = ", total_delta / (num_months - 1))
    print(f"Greatest Increase in Profits: {max_month} (${max_delta})")
    print(f"Greatest Decrease in Profits: {min_month} (${min_delta})")