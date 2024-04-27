import csv
import os

csvpath = os.path.join(".", "Resources", "budget_data.csv")

outputFile = os.path.join("./Analysis/FinancialAnalysis.txt")

totalMonths = 0
totalProfitLoss = 0
monthlyChanges = []
months =[]

with open(csvpath) as budget_data:
    csvreader = csv.reader(budget_data)
    header = next(csvreader)
    firstRow = next(csvreader)
    totalMonths += 1
    totalProfitLoss += float(firstRow[1])
    previousProfitLoss = float(firstRow[1])

    for row in csvreader:
        totalMonths += 1
        totalProfitLoss += float(row[1])
        netChange = float(row[1]) - previousProfitLoss
        monthlyChanges.append(netChange)
        months.append(row[0])
        previousProfitLoss = float(row[1])

averageChange = sum(monthlyChanges) / len(monthlyChanges)

greatestIncrease = [months[0], monthlyChanges[0]]
greatestDecrease = [months[0], monthlyChanges[0]]

for m in range(len(monthlyChanges)):
    if(monthlyChanges[m] > greatestIncrease[1]):
        greatestIncrease[1] = monthlyChanges[m]
        greatestIncrease[0] = months[m]
    if(monthlyChanges[m] < greatestDecrease[1]):
        greatestDecrease[1] = monthlyChanges[m]
        greatestDecrease[0] = months[m]
        
output = (
    f"\nFinancial Analysis \n"
    f"-----------------------------\n"
    f"\tTotal Months = {totalMonths} \n"
    f"\tTotal = ${totalProfitLoss:,.2f} \n"
    f"\tAverage Change = ${averageChange:,.2f} \n"
    f"\tGreatest Increase in Profits = {greatestIncrease[0]} (${greatestIncrease[1]:,.2f}) \n"
    f"\tGreatest Decrease in Profits = {greatestDecrease[0]} (${greatestDecrease[1]:,.2f}) \n"
    )

print(output)

with open(outputFile, "w") as textFile:
    textFile.write(output)