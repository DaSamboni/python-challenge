#Dependencies
import os
import csv

csv_path = os.path.join('Resources', "election_data.csv")

candidates = []
voters = []
vote_percentages = []
vote_counts = {}


with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader, None)

    for row in csvreader:
      voters.append(row[0])

      if row[2] not in vote_counts:
            vote_counts[row[2]] = 0
            candidates.append(row[2])

      vote_counts[row[2]] += 1


total_votes = len(voters)
for x in vote_counts.values():
    vote_percentages.append(x/total_votes*100)
vote_percentages = [round(percent, 2) for percent in vote_percentages]


totals = []
for x in vote_counts.values():
    totals.append(x)


election_results = []
for x in range(len(candidates)):
    election_results.append(f"{candidates[x]}: {vote_percentages[x]} ({totals[x]})")


most_votes = max(vote_counts.values())
election_winner = [k for k, v in vote_counts.items() if v == most_votes]


output_data = "Election Results\n"
output_data += "--------------------------\n"
output_data += f"Total Votes: {total_votes}\n"
output_data += "--------------------------\n"
for x in election_results:
    output_data += f"{x}\n"
output_data += "--------------------------\n"
output_data += f"Winner: {election_winner}\n"
output_data += "--------------------------"

print(f"{output_data}")

output_path = os.path.join("analysis2", "pypoll_analysis.txt")
report = open(output_path, 'w')
report.write(output_data)
report.close
