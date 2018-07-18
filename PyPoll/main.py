import pandas as pd
import numpy as np
# Reference the file where the CSV is located
file = 'election_data.csv'
# Import the data into a Pandas DataFrame
df = pd.read_csv(file)
df.head()
print("Election Results")
print("-------------------------")
vote_number = df["Voter ID"].count()
print(f"Total Votes: {vote_number}")
print("-------------------------")
df_final = df["Candidate"].value_counts()
df_sum = sum(df_final)
max_num = df_final.max()
candidate_name = df_final.index
i = 0
result = []
for x in df_final:
    rate = round(x/df_sum * 100,4)
    print(f"{candidate_name[i]}: {rate}% ({x})")
    result.append(x)
    i += 1
print("-------------------------")
winner_name = candidate_name[result.index(max_num)]
print(f"Winner: {winner_name}")
print("-------------------------")
with open("output.txt","w") as writer:
    writer.write("Election Results\n")
    writer.write("-------------------------\n")
    writer.write(f"Total Votes: {vote_number}\n")
    writer.write("-------------------------\n")
    i = 0
    for x in df_final:
        rate = round(x/df_sum * 100,4)
        writer.write(f"{candidate_name[i]}: {rate}% ({x})\n")
        i += 1
    writer.write("-------------------------\n")
    writer.write(f"Winner: {winner_name}\n")
    writer.write("-------------------------\n")