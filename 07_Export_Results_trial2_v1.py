"""Component 07 Export Results trial 2 version 1
the user inputs a filename (assume valid data)
non valid input for filename will be dealt with in later versions
this trial writes the data to csv with each question on a new row
this trial also includes headings for each data type on the first row
"""

import csv

# list of results for export (just used for testing)
results = ['5 + 1 = ', 6, 'Correct', 6], ['1 + 2 = ', 3, 'Correct', 3], \
          ['0 + 5 = ', 5, 'Correct', 5], \
          ['5 + 0 = ', 5, 'Correct', 5], ['10 + 10 = ', 20, 'Correct', 20], \
          ['5 + 3 = ', 8, 'Correct', 8], \
          ['6 + 10 = ', 16, 'Correct', 16], ['4 + 7 = ', 11, 'Correct', 11], \
          ['2 + 8 = ', 10, 'Correct', 10], \
          ['2 + 3 = ', 5, 'Correct', 5]

# Get filename, can't be blank / invalid
# assume valid data for now.
filename = input("Enter a Filename: ")
filename += ".csv"

# List of data type headers
Details = ['Question', 'Your Answer', 'Mark', 'Correct Answer']
with open(filename, 'w', newline='') as f:
    write = csv.writer(f)
    write.writerow(Details)  # writes data type headers
    write.writerows(results)  # writes results
