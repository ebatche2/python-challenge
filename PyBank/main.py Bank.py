import csv
import pandas as pd

csv_path = "resources/budget_data.csv"

df = pd.read_csv(csv_path)

print(df.head())

total_months = 0
net_profit_loss = 0
previous_profit_loss = 0
profit_loss_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]


with open(csv_path, "r") as file:
    csv_reader = csv.reader(file)

    header = next(csv_reader)

    for row in csv_reader:

        total_months += 1

        profit_loss = int(row[1])

        net_profit_loss += profit_loss

        if total_months > 1:
            profit_loss_change = profit_loss - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)

            if profit_loss_change > greatest_increase[1]:
                greatest_increase = [row[0], profit_loss_change]
            if profit_loss_change < greatest_decrease[1]:
                greatest_decrease = [row[0], profit_loss_change]
        
        previous_profit_loss = profit_loss
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${average_change: .2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

outputpath = "output.txt"
with open(outputpath, "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${net_profit_loss}\n")
    textfile.write(f"Average Change: ${average_change: .2f}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
