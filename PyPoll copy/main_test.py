import csv
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "Resources\\election_data.csv")


with open(filename) as csv_file:
    csvreader = csv.reader(csv_file, delimiter= ",")
    #print(csvreader)
    header = next(csvreader)

    ballot_ind = header.index("Ballot ID")
    county_ind = header.index("County")
    candidate_ind = header.index("Candidate")

    total_votes = 0
    vote_getters = 0
    candidate = 0
    winner_vote_count = 0
    winner = ""

    candidate_votes = {
        'Charles Casper Stockham': 0,
        'Diana DeGette': 0,
        'Raymon Anthony Doane': 0
    }

    for row in csvreader:
        candidate = row[candidate_ind]
        total_votes += 1

        candidate_votes[candidate] = candidate_votes[candidate] + 1

    for name in candidate_votes:
        if winner_vote_count < candidate_votes[name]:
            winner_vote_count = candidate_votes[name]
            winner = name


with open("election_results.txt", "w")as out_file:
    #exporting results to .txt file
    out_file.write("Election Results\n")
    out_file.write("------------------------------\n")
    out_file.write(f"Total Votes: {total_votes}\n")
    out_file.write("------------------------------\n")
    #printing results for terminal
    print("Election Results\n")
    print("------------------------------\n")
    print(f"Total Votes: {total_votes}\n")
    print("------------------------------\n")
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percentage = round(100*votes/total_votes, 3)

        print(f"{candidate}: {percentage}% votes ({votes})\n")
        out_file.write(f"{candidate}: {percentage}% votes ({votes})\n")

    print("------------------------------\n")
    print(f"Winner: {winner}\n")
    print("------------------------------\n")

    out_file.write("------------------------------\n")
    out_file.write(f"Winner: {winner}\n")
    out_file.write("------------------------------\n")