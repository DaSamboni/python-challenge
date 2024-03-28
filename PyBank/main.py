#Dependencies
import os
import csv

#CSV path
csv_path = os.path.join('Resources', 'budget_data.csv')

#Lists for later
dates = []
profit_loss = []
monthly_change = []

with open(csv_path, newline = "") as csvfile:
  csvreader = csv.reader(csvfile, delimiter = ',')
  next(csvreader, None)

  for row in csvreader:
    dates.append(row[0])
    profit_loss.append(row[1])
    
profit_loss = list(map(int, profit_loss))
month_total = len(profit_loss)
total_profit = sum(profit_loss)

for x in range(1,len(profit_loss)):
    monthly_change.append(profit_loss[x] - profit_loss[x-1])

total_revenue = sum(monthly_change)
average_change = round((total_revenue / month_total),2)

largest_increase = max(monthly_change)
largest_decrease = min(monthly_change)


largest_increase_date = date[monthly_change.index(max(monthly_change))]
largest_decrease_date = date[monthly_change.index(min(monthly_change))]


complete_data = (
  f"Financial Analysis\n"
  f"-------------------------------------\n"
  f"Total Months: {month_total}\n"
  f"Total: ${total_profit}\n"
  f"Average Change: ${average_change}\n"
  f"Greatest Increase in Profits: {largest_increase_date} ${largest_increase}\n"
  f"Greatest Decrease in Profits: {largest_decrease_date} ${largest_decrease}\n")
print(complete_data)

output_path = os.path.join("analysis", "pybank_analysis.txt")
report = open(output_path, 'w')
report.write(complete_data)
report.close
  




  
