import os 
import csv

PyBank = os.path.join('..', 'Resources', 'budget_data.csv')

change = []
months = []
profit = []

with open("budget_data.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    
    for row in csvreader:
        months.append(row[0])
        profits.append(row[1])
       
    total_months = len(months)
    total_profit = sum(profit)

    for i in range(1, len(profit)):
        change.append((int(profit[i]) - int(profit[i-1])))

average_change = sum(change) / len(change)

greatest_profit_increase_index = max(change)
greatest_profit_decrease_index = min(change)

print("Financial Analysis")
print("-----------------------------")
print("Total months: " + str(total_months))
print("Total profits: " + str(profit)) 
print("Average change: " + str(average_change))
print("Greatest Increase in Profits: " + str(greatest_profit_increase_index))
print("Greatest Decrease in Profits: " + str(greatest_profit_decrease_index))
text_export = os.path.join(`budget_data.csv`)

with open("Bank_Analysis.txt", "w") as txt_file:
    csv_writer = csv.writer(txt_file)

csv_writer.writerow("Financial Analysis")
csv_writer.writerow("---------------------------")
   # csv_writer.writerow("Total months: {len(months)-1:,])
   # csv_writer.writerow([f"Total profits: ${total_profit:,}"])
    #csv_writer.writerow([f"Average Change: ${average_change:,}"])
   # csv_writer.writerow([f"Greatest Increase in Profits: {months[offset_greatest_increase]} (${max(changes):,})"])
    #csv_writer.writerow([f"Greatest Decrease in Profits: {months[offset_greatest_decrease]} (${mix(changes):,})"])


