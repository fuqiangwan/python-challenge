import pandas as pd
import numpy as np
# Reference the file where the CSV is located
file = 'budget_data.csv'
# Import the data into a Pandas DataFrame
df = pd.read_csv(file)
df.head()
total_month = df["Date"].count()
print ("Financial Analysis")
print ("----------------------------")
print (f"Total Month: {total_month}")
total_amount = df["Revenue"].sum()
print (f"Total : ${total_amount}")
aver_change = round(df["Revenue"].mean(),2)
print (f"Average  Change: ${aver_change}")
max_date = df["Date"].max()
max_revenue = df["Revenue"].max()
print (f"Greatest Increase in Profits: {max_date} (${max_revenue})")
min_date = df["Date"].min()
min_revenue = df["Revenue"].min()
print (f"Greatest Decrease in Profits: {min_date} (${min_revenue})")
with open("output.txt","w") as writer:
    writer.write("Financial Analysis\n")
    writer.write("----------------------------\n")
    writer.write(f"Total Month: {total_month}\n")
    writer.write(f"Total : ${total_amount}\n")
    writer.write(f"Average  Change: ${aver_change}\n")
    writer.write(f"Greatest Increase in Profits: {max_date} (${max_revenue})\n")
    writer.write(f"Greatest Decrease in Profits: {min_date} (${min_revenue})\n")