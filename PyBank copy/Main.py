import csv
import os

#Pulling csv file to access data.
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "Resources\\budget_data.csv")

# Opening CSVReader and telling code to not count the header row in counts.
with open(filename) as csv_file:
    csvreader = csv.reader(csv_file, delimiter= ",")
    header = next(csvreader)
    
    # Setting Indexes
    date_ind = header.index("Date")
    profit_loss_ind = header.index("Profit/Losses")
    # profit_loss_changes = header.index("Change")

# Setting Variables:
    first_line = next(csvreader)
    total_months = 1
    net_total = int(first_line[profit_loss_ind])
    profit_loss_changes = 0
    profit_loss = int(first_line[profit_loss_ind])
    greatest_profit = 0
    greatest_loss = 0
    greatest_profit_date = ""
    greatest_loss_date = ""

# Work for Analysis Data:
    for row in csvreader:
        total_months  += 1
        current_date = str(row[date_ind])
        net_total += int(row[profit_loss_ind])
        next_profit_loss = int(row[profit_loss_ind])
        difference = next_profit_loss - profit_loss
        profit_loss_changes += difference
        profit_loss = next_profit_loss
        if difference > greatest_profit:
            greatest_profit = difference
            greatest_profit_date = current_date
        if difference < greatest_loss:
            greatest_loss = difference
            greatest_loss_date = current_date
#printing results
print("Financial Analysis\n")
print("------------------------------\n")
print(f"Total Months: {total_months}\n")
print(f"Total:  ${net_total}\n")
print(f"Average Change: ${round(profit_loss_changes/(total_months-1), 2)}\n")
print(f"Greatest Increase in Profits: {greatest_profit_date} (${greatest_profit})\n")
print(f"Greatest Decrease in Profits: {greatest_loss_date} (${greatest_loss})\n")
#creating and printing results to a .txt file
with open("PyBank_Data_Analysis.txt", "w")as out_file:
    out_file.write("Financial Analysis\n")
    out_file.write("------------------------------\n")
    out_file.write(f"Total Months: {total_months}\n")
    net_total_string = '${:,.2f}'.format(net_total)
    out_file.write(f'Total: {net_total_string }\n')
    out_file.write(f'Average Change: ${round(profit_loss_changes/(total_months-1), 2)}\n')
    out_file.write(f"Greatest Increase in Profits: {greatest_profit_date} (${greatest_profit})\n")
    out_file.write(f"Greatest Decrease in Profits: {greatest_loss_date} (${greatest_loss})")
