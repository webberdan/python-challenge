"""This script analyzes finaincial data
dataset provided is in csv format, and has two columns "Date" and "Profit/Loss" 

    Requirements:
        Find total number of months in dataset
        Net amount of profit/loss from period
        find month with greatest increase in profit (display date and total)
        find month with greatest decrease in profit (display date and total)
"""

# import os module for file pathing
import os

# import the csv module for us to handle .csv files
import csv

# create path to csv file
filePath = os.path.join("./", "Resources", "budget_data.csv")

#create a output file to export results to:
outputFile = os.path.join("./", "Analysis", "PyBankResults.txt")

"""print("filePath generated: " + filePath)
# = "Resources\budget_data.csv"""

"""print(filePath)"""

# Open the csv file from path
with open(filePath, 'r', encoding="utf-8") as csvfile:

    # read file
    csvReader = csv.reader(csvfile, delimiter=",")

    # Skip Header
    csvheader = next(csvReader)

    totalMonths = 0
    totalValue = 0

    # for average changes between months, create lists to store values
    averageChangeValueList = []
    averageChangeDateList = []

    for index, row in enumerate(csvReader):
        # if is NOT first row (index > 0)
        if index > 0:
            diff = int(row[1]) - int(previousValue)
            averageChangeValueList.append(diff)
            averageChangeDateList.append(row[0])
        # increment totalMonths since each row is a new month's entry, this gives total months in dataset
        totalMonths += 1

        # add current value to total value to keep track of it
        totalValue = totalValue + int(row[1])
        averageChange = totalValue
        # set previous value to current value for next time through loop to diff
        previousValue = row[1]

    # average change, declare starting values for variables
    averageChange = 0
    greatestIncreaseValue = 0
    greatestDecreaseValue = 0

    #loop to begin calculating average increase or decrease and storing values
    for index, v in enumerate(averageChangeValueList):
        averageChange += v
        
        if v > greatestIncreaseValue:
            greatestIncreaseValue = v
            greatestIncreaseDate = averageChangeDateList[index]
        if v < greatestDecreaseValue:
            greatestDecreaseValue = v
            greatestDecreaseDate = averageChangeDateList[index]

        totalAverageChange = averageChange / len(averageChangeValueList)
    
    output = (

        f"\n\nFinancial Analysis\n"
        f"----------------------------\n"
        f"\ttotal months: {totalMonths}\n"
        f"\ttotal value: {totalValue}\n"
        f"\ttotal average change: {totalAverageChange}\n"
        f"\tgreatest increase: {greatestIncreaseValue} on {greatestIncreaseDate}\n"
        f"\tgreatest decrease: {greatestDecreaseValue} on {greatestDecreaseDate}\n"

    )    
    
    
    print(output)
    
    with open(outputFile, 'w') as textFile:
        #Write output data to the text file
        textFile.write(output)
    
