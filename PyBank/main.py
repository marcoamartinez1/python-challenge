#modules
import os
import csv
import sys

#finds CSV
csvpath = os.path.join("Resources", "budget_data.csv")

#initializes variables
month_count = 0
total_profit = 0
max_profit = -99999999
min_profit = 99999999
max_date = ""
min_date = ""
max_list = []
min_list = []
change = 0
change_list = []
minimum_change = [10000000000, ""]
maximum_change = [-10000000000,""]
# opens the file
prev_value = 0
with open(csvpath, "r", encoding='UTF-8') as csvfile:
     csvreader = csv.reader(csvfile, delimiter = ",")
    #skips header
     csv_header = next(csvfile)
     #iterates through data
     for row in csvreader:
        #updates the month count for each iteration
        month_count += 1
        #updates the profit count for each iteration
        total_profit += int(row[1])
        #after the first month, finds the change between each month
        if month_count > 1:
            current_value = int(row[1])
            change = current_value - prev_value
            change_list.append(change)
            #finds max and min changes and the respective months
            if change > maximum_change[0]:
                maximum_change = [change, str(row[0])]
            if change < minimum_change[0]:
                minimum_change = [change, str(row[0])]
       #finds the month with the most profit
        if int(row[1]) > max_profit:
            max_profit = int(row[1])
            max_date = str(row[0])
            max_list = [max_date, max_profit]
        #finds the month with the least profit
        if int(row[1]) < min_profit:
            min_profit = int(row[1])
            min_date = str(row[0])
            min_list = [min_date, min_profit]
        prev_value = int(row[1])


#initializes variables to be used to find average changes
total_change = 0
total_average = 0
#iterates through the list of month to month changes, sums the changes, and then divides them by the length of the list to find the average
for item in change_list:
    total_change += item
total_average = round(total_change/len(change_list),2)

with open('PyBank.txt', 'w') as f: 
#prints results to terminal and file

    print("Financial Analysis", file=sys.stdout)
    print("----------------------------", file=sys.stdout)
    print(f"Total Months: {month_count}", file=sys.stdout)
    print(f"Total: ${total_profit}", file=sys.stdout)
    print(f"Average Change: ${total_average}", file=sys.stdout)
    print(f"Greatest Increase in Profits: {maximum_change[1]} (${maximum_change[0]})", file=sys.stdout)
    print(f"Greatest Decrease in Profits: {minimum_change[1]} (${minimum_change[0]})", file=sys.stdout)
    print(f"The month with the most profit was {max_date} with a profit of ${max_profit}", file=sys.stdout)
    print(f"The month with the least profit was {min_date} with a profit of ${min_profit}", file=sys.stdout)

    # Print to the file only
    print("Financial Analysis", file=f)
    print("----------------------------", file=f)
    print(f"Total Months: {month_count}", file=f)
    print(f"Total: ${total_profit}", file=f)
    print(f"Average Change: ${total_average}", file=f)
    print(f"Greatest Increase in Profits: {maximum_change[1]} (${maximum_change[0]})", file=f)
    print(f"Greatest Decrease in Profits: {minimum_change[1]} (${minimum_change[0]})", file=f)
    #resets the standard output
    sys.stdout = sys.__stdout__