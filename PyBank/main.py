import os 
import csv

csvpath = os.path.join("Resources/budget_data.csv")

change = []
months = []
profit = []

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    header = next(csvreader)
    
    for row in csvreader:
        months.append(row[0])
        profit.append(row[1])
       
    total_months = len(months)
    total_profit = len(profit)

    for i in range(1, len(profit)):
        change.append((int(profit[i]) - int(profit[i-1])))

average_change = sum(change) / len(change)

greatest_profit_increase_index = max(change)
greatest_profit_decrease_index = min(change)

print("Financial Analysis")
print("-----------------------------")
print("Total months: " + str(total_months))
print("Total profits: " + str(profit)) 
print("Average change: $" + str(average_change))
print("Greatest Increase in Profits: $" + str(greatest_profit_increase_index))
print("Greatest Decrease in Profits: $" + str(greatest_profit_decrease_index))

output_file = os.path.join("Resources/Bank_Analysis.txt")

with open(output_file, "w") as txt_file:
    csv_writer = csv.writer(txt_file)

csv_writer.writerow("Financial Analysis")
csv_writer.writerow("---------------------------")
csv_writer.writerow("Total months: " + str(total_months))
csv_writer.writerow("Total profits: " + str(profit))
csv_writer.writerow("Average change: " + str(average_change))
csv_writer.writerow("Greatest Increase in Profits: " + str(greatest_profit_increase_index))
csv_writer.writerow("Greatest Decrease in Profits: " + str(greatest_profit_decrease_index))



