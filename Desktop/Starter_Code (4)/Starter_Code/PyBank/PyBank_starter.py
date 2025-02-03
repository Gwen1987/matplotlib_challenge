# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = r'C:\python_challenge\Starter_Code (4)\Starter_Code\PyBank\Resources\budget_data.csv' # Input file path C:\python_challenge\Starter_Code (4)\Starter_Code\PyBank\Resources\budget_data.csv'
file_to_output =r'C:\python_challenge\Starter_Code (4)\Starter_Code\PyBank\analysis\budget_analysis.txt'  # Output file path
os.makedirs(os.path.dirname(r'C:\python_challenge\Starter_Code (4)\Starter_Code\PyBank\analysis\budget_analysis.txt'), exist_ok=True)

# Define variables to track the financial data
total_months = 0
total_net = 0
#average_change = total_net/total_months
Greatest_months = 0
Greatest_Decrease = 0

# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load, encoding='UTF-8') as financial_data:
    reader = csv.reader(financial_data, delimiter=",")
    
    

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list


    # Track the total and net change


    # Process each row of data
    for row in reader:
        print(row)

        # Track the total


        # Track the net change


        # Calculate the greatest increase in profits (month and amount)


        # Calculate the greatest decrease in losses (month and amount)



# Calculate the average net change across the months


# Generate the output summary


# Print the output


# Write the results to a text file
#with open(file_to_output, "w") as txt_file:
 #   txt_file.write(output)
