#modules
import os
import csv
import sys

#finds CSV
csvpath = os.path.join("Resources", "election_data.csv")

#initialize variables
total_votes = 0
doane_votes = 0
degette_votes = 0
stockham_votes = 0
doane_percent = 0
degette_percent = 0
stockham_percent = 0
winner = ""

#opens CSV
with open(csvpath, "r", encoding='UTF-8') as csvfile:
     csvreader = csv.reader(csvfile, delimiter = ",")
     csv_header = next(csvfile)
     #iterates through the data
     for row in csvreader:
        #updates the total votes for each iteration
        total_votes +=1
        #if a candidate name appears in an iteration, their respective count is updated
        if row[2] == "Raymon Anthony Doane":
            doane_votes += 1
        if row[2] == "Diana DeGette":
            degette_votes += 1
        if row[2] == "Charles Casper Stockham":
            stockham_votes += 1

#find percentage of total vote for each candidate
doane_percent = round((doane_votes/total_votes)*100,3)
degette_percent = round((degette_votes/total_votes)*100,3)
stockham_percent = round((stockham_votes/total_votes)*100,3)

#compare vote counts to find winner
if doane_votes > degette_votes and doane_votes > stockham_votes:
    winner = "Raymon Anthony Doane"
if degette_votes > doane_votes and degette_votes > stockham_votes:
    winner = "Diana DeGette"
if stockham_votes > doane_votes and stockham_votes > degette_votes:
    winner = "Charles Casper Stockham"

#creates .txt file
with open('PyPoll.txt', 'w') as f:
#print results
    print("Election Results", file=sys.stdout)
    print("----------------------", file=sys.stdout)
    print(f"Total votes: {total_votes}", file=sys.stdout)
    print("----------------------", file=sys.stdout)
    print(f"Charles Casper Stockham: {stockham_percent}% ({stockham_votes})", file=sys.stdout)
    print(f"Diana DeGette: {degette_percent}% ({degette_votes})", file=sys.stdout)
    print(f"Raymon Anthony Doane: {doane_percent}% ({doane_votes})", file=sys.stdout)
    print("----------------------", file=sys.stdout)
    print(f"Winner: {winner}", file=sys.stdout)
    print("----------------------", file=sys.stdout)

    print("Election Results", file=f)
    print("----------------------", file=f)
    print(f"Total votes: {total_votes}", file=f)
    print("----------------------", file=f)
    print(f"Charles Casper Stockham: {stockham_percent}% ({stockham_votes})", file=f)
    print(f"Diana DeGette: {degette_percent}% ({degette_votes})", file=f)
    print(f"Raymon Anthony Doane: {doane_percent}% ({doane_votes})", file=f)
    print("----------------------", file=f)
    print(f"Winner: {winner}", file=f)
    print("----------------------", file=f)
#exports a text file per submission instructions
sys.stdout = sys.__stdout__