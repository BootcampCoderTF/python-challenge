import os
import csv


# Collect data from the Resources folder
budget_csv = os.path.join('PyBank', 'Resources', 'budget_data.csv')

# Initialize a variable to store the row count minus the column header
total_rows = -1

# Open the CSV file for reading
with open(budget_csv, 'r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)    
    # Iterate through the rows in the CSV file
    for row in csv_reader:
        total_rows += 1

# --------------FIND THE TOTAL OF PROFIT/LOSS------------------
# -------------------------------------------------------------

# From the total month count we know the row count in the file
cell_range = 'B2:B87'

# Initialize a variable to store the sum
total_ProfitLoss = 0

# Open the CSV file for reading
with open(budget_csv, 'r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)
    
    # Iterate through the rows in the CSV file
    for row in csv_reader:
        for cell in row:
            try:
                # Convert the cell value to a float
                number = float(cell)
                total_ProfitLoss += number
            except ValueError:
                # If the conversion to float fails, continue to the next cell
                continue

# Convert to dollar format using the format function
total_ProfitLoss_df = "${:.2f}".format(total_ProfitLoss)


# ------------FIND THE AVERAGE OF THE DIFFERENCE---------------
# -------------------------------------------------------------

# Initialize the start and end row and column indices start is B2 and end is B87
start_row, start_col = 2, 2
end_row, end_col = 87, 2

# Initialize a variable to store the differences and the previous cell's value
differences = []
previous_value = None
max_row = None
min_row = None

# Open the CSV file for reading
with open(budget_csv, 'r') as file:
    csv_reader = csv.reader(file)

    # Iterate through the rows and columns in the specified cell range
    for row_num, row in enumerate(csv_reader, start=1):
        try:
            # Extract the value from the specified column
            value = float(row[start_col - 1])
            if start_row <= row_num <= end_row:
                if previous_value is not None:
                    difference = value - previous_value
                    differences.append(difference)
                previous_value = value
        except (ValueError, IndexError):
            # For times where the cell value is not a valid number
            continue

difference_sum = sum(differences)

# Calculate the average by dividing the sum by the total number of rows
average__of_difference = difference_sum / len(differences)
average__of_difference = "${:.2f}".format(average__of_difference)
max_difference = max(differences)
max_difference = "${:.2f}".format(max_difference)
min_difference = min(differences)
min_difference = "${:.2f}".format(min_difference)

# -------------------PRINT THE RESULTS-------------------------
# -------------------------------------------------------------

# Print the total number of rows i.e months
print("Total months in the data:", total_rows)

# Print the total sum of the profits/losses
print(f"Total sum of selected cell range: {total_ProfitLoss_df}")

# Print the average difference
print("The average of the differences is:", average__of_difference)

# Print the max/min differences
print(f"the maximum increase is: {max_difference}")
print(f"the maximum decrease is: {min_difference}")

# --------------------WRITE THE RESULTS------------------------
# -------------------------------------------------------------

# Values to write into the results file
results = "Financial Analysis \n \n"
results += "---------------------------- \n \n"
results += f"Total months analysed: {total_rows} \n \n"
results += f"Total sum of Money: {total_ProfitLoss_df} \n \n"
results += f"The Average Change: {average__of_difference} \n \n"
results += f"The Greatest Increase in Profits: {max_difference} \n \n"
results += f"The Greatest Decrease in Profits: {min_difference} \n \n"
results += "----------------------------"

# File path for the new text file
output_file_path = os.path.join("PyBank", "analysis", "output.txt")

# Open the file for writing
with open(output_file_path, 'w') as file:
    # Write the results to the file
    file.write(results)

# Print Confirmation into the terminal
print(f"Results have been saved to {output_file_path}")