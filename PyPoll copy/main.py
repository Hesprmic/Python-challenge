import csv
import os
#the path for our csv file
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "Resources\\election_data.csv")

#opening file and reading csv to pull data for analysis
with open(filename) as csv_file:
    csvreader = csv.reader(csv_file, delimiter= ",")
    header = next(csvreader)
    #create index for referencing data from csv
    ballot_ind = header.index("Ballot ID")
    county_ind = header.index("County")
    candidate_ind = header.index("Candidate")
    #variable creation
    total_votes = 0
    candidate = 0
    winner_vote_count = 0
    winner = ""

    candidate_votes = {
        'Charles Casper Stockham': 0,
        'Diana DeGette': 0,
        'Raymon Anthony Doane': 0
    }
    #for loop to pull data from index to complete instructions for module (tabulation of total votes)
    for row in csvreader:
        candidate = row[candidate_ind]
        total_votes += 1

        candidate_votes[candidate] = candidate_votes[candidate] + 1
    #for loop to set up results to determine winner
    for name in candidate_votes:
        if winner_vote_count < candidate_votes[name]:
            winner_vote_count = candidate_votes[name]
            winner = name

#creating text file and printing all results
with open("election_results.txt", "w")as out_file:
    #printing total votes results to .txt file
    out_file.write("Election Results\n")
    out_file.write("------------------------------\n")
    out_file.write(f"Total Votes: {total_votes}\n")
    out_file.write("------------------------------\n")
    #printing total votes results for terminal
    print("Election Results\n")
    print("------------------------------\n")
    print(f"Total Votes: {total_votes}\n")
    print("------------------------------\n")
    #created for loop to calculate votes for each of the candidates and their percentage of the vote they received
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percentage = round(100*votes/total_votes, 3)

        print(f"{candidate}: {percentage}% votes ({votes})\n")
        out_file.write(f"{candidate}: {percentage}% votes ({votes})\n")

    #declaring winner of the election
    print("------------------------------\n")
    print(f"Winner: {winner}\n")
    print("------------------------------\n")

    out_file.write("------------------------------\n")
    out_file.write(f"Winner: {winner}\n")
    out_file.write("------------------------------\n")