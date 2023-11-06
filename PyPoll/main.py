import os
import csv


# Collect data from the Resources folder
votes_csv = os.path.join('PyPoll', 'Resources', 'election_data.csv')

# Lists to store data from the csv file
ballot = []
county = []
candidate = []

# Initialize a variable to store the row count minus the column header
total_rows = -1

# Open the CSV file for reading
with open(votes_csv, 'r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)    
    # Iterate through the rows in the CSV file
    for row in csv_reader:
        total_rows += 1
        # Add ballot i.d
        ballot.append(row[0])

        # Add county
        county.append(row[1])

        # Add candidate
        candidate.append(row[2])

# -------------------CALCULATE UNIQUE VOTES--------------------
# -------------------------------------------------------------

# Specify the index of the column you want to analyze
column_index = 0  # Skip the first row (header)

# Create a data set to store unique values
candidate_name = set()

# Create a dictionary to store value counts
value_counts = {}

# Iterate through the list and counts how many times each unique value appears
for value in candidate[1:]:
    if value in value_counts:
        value_counts[value] += 1
    else:
        value_counts[value] = 1

# Print the counts of unique values
for value, count in value_counts.items():
    value_percent = count / total_rows * 100
    print(f"The candidate '{value}' appears {count} times in the file.({value_percent:.2f}%)")


# Iterate through the list and count the occurrences of each candidate
for value in candidate:
    if value in value_counts:
        value_counts[value] += 1
    else:
        value_counts[value] = 1

# Find the candidate with the highest count
most_common_value = max(value_counts, key=value_counts.get)

# -------------CALCULATE EACH CANDIDATES VOTES-----------------
# -------------------------------------------------------------

# Value of the first candidate
target_value_a = "Charles Casper Stockham"
# Use the count() method to count the occurrences of the target value
count_a = candidate.count(target_value_a)
# Calculate the percentage target value
percentage_a = (count_a / total_rows) * 100

# Value of the second candidate
target_value_b = "Diana DeGette"
# Use the count() method to count the occurrences of the target value
count_b = candidate.count(target_value_b)
# Calculate the percentage target value
percentage_b = (count_b / total_rows) * 100

# Value of the third candidate
target_value_c = "Raymon Anthony Doane"
# Use the count() method to count the occurrences of the target value
count_c = candidate.count(target_value_c)
# Calculate the percentage target value
percentage_c = (count_c / total_rows) * 100


# -------------------PRINT THE RESULTS-------------------------
# -------------------------------------------------------------

# Print the total number of rows i.e votes
print("Total votes in the file:", total_rows)

# Print the most common value and its count
print(f"Candidate with the most votes is: {most_common_value} ")

# --------------------WRITE THE RESULTS------------------------
# -------------------------------------------------------------

# Values to write into the results file
results = "Election Results \n \n"
results += "---------------------------- \n \n"
results += f"Total votes: {total_rows} \n \n"
results += f"{target_value_a}: {percentage_a:.2f}% ({count_a} votes) \n \n"
results += f"{target_value_b}: {percentage_b:.2f}% ({count_b} votes) \n \n"
results += f"{target_value_c}: {percentage_c:.2f}% ({count_c} votes) \n \n"
results += "---------------------------- \n \n"
results += f"Winner: {most_common_value} \n \n"
results += "----------------------------"

# File path for the new text file
output_file_path = os.path.join("PyPoll", "analysis", "output.txt")

# Open the file for writing
with open(output_file_path, 'w') as file:
    # Write the results to the file
    file.write(results)

# Print confirmation into the terminal
print(f"Results have been saved to {output_file_path}")