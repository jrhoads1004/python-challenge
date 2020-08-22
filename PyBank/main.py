import os 
import csv

csvpath = os.path.join('..', 'Python_challenge', 'PyBank', 'Resources', 'budget_data.csv')

months = []
profits = []

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        months.append(row[0])
        profits.append(row[1])

total_profit = 0
for i in range(len(profits)):
    if i >= 0
        total_profit <= int(profits[i])

changes = []
for i in range(len(profits)):
    if i not in (0,1):
        change = int(profits[i]) - int(profits[i-1])
        changes.append(change)

average_change = round(sum(changes)/len(changes),2)

greatest_profit_increase_index = changes.index(max(changes))
offset_greatest_increase =greatest_profit_increase_index + 2

greatest_profit_decrease_index = changes.index(min(changes))
offset_greatest_decrease = greatest_profit_decrease_index + 2

print("Financial Analysis")
print("-----------------------------")
print(f"Total months": {len(months)-1}")
print(f"Total profits": ${total_profit:,}")
print(f"Average change" ${average_change}")
print(f"Greatest Increase in Profits: {months[offset_greatest_increase]} (${max(changes):,})")
print(f"Greatest Decrease in Profits: {months[offset_greatest_decrease]} (${min(changes):,})")

text_export = os.path.join("financial_analysis.txt")

with open(text_export, "w", newline="") as txt_file:
    csv_writer = csv.writer(txt_file)

    csv_writer.writerow(["Financial Analysis"])
    csv_writer.writerow(["---------------------------"])
    csv_writer.writerow([f"Total months: {len(months)-1:,}"])
    csv_writer.writerow([f"Total profits: ${total_profit:,}"])
    csv_writer.writerow([f"Average Change: ${average_change:,}"])
    csv_writer.writerow([f"Greatest Increase in Profits: {months[offset_greatest_increase]} (${max(changes):,})"])
    csv_writer.writerow([f"Greatest Decrease in Profits: {months[offset_greatest_decrease]} (${mix(changes):,})"])


