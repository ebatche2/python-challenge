import csv
import pandas as pd

df = pd.read_csv("resources/election_data.csv")

total_votes = df["Ballot ID"].count()

candidate_list = df["Candidate"].unique()

vote_counts = df["Candidate"].value_counts()
vote_percentages = (vote_counts / total_votes) * 100

candidate_votes = vote_counts.to_dict()

winner = vote_counts.idxmax()

print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
for candidate in candidate_list:
    print(f"{candidate}: {vote_percentages[candidate]: .3f}% ({candidate_votes[candidate]})")
print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")