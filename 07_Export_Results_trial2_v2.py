"""Component 07 Export Results trial 2 version 2
this carries on from version 1
but now checks filename to make sure it is valid
uses regular expression module to check for invalid char's in the filename
(only letters, numbers, or underscores allowed)
"""

import csv
import re  # Imports the regular expression library re

# list of results for export (just used for testing)
results = ['5 + 1 = ', 6, 'Correct', 6], ['1 + 2 = ', 3, 'Correct', 3], \
          ['0 + 5 = ', 5, 'Correct', 5], \
          ['5 + 0 = ', 5, 'Correct', 5], ['10 + 10 = ', 20, 'Correct', 20], \
          ['5 + 3 = ', 8, 'Correct', 8], \
          ['6 + 10 = ', 16, 'Correct', 16], ['4 + 7 = ', 11, 'Correct', 11], \
          ['2 + 8 = ', 10, 'Correct', 10], \
          ['2 + 3 = ', 5, 'Correct', 5]

# Get filename, can't be blank / invalid
filename = ""
has_error = "yes"
while has_error == "yes":
    problem = ""
    has_error = "no"
    filename = input("Enter a Filename: ")

    # Regular expression to check file name
    # Can be Upper or lower case letters, numbers or underscores
    valid_char = "[A-Za-z0-9_]"
    for letter in filename:
        if re.match(valid_char, letter):
            continue  # If the letter is valid, goes back and checks the next

        # No spaces allowed
        elif letter == " ":  # otherwise, find problem
            problem = "(spaces not allowed)"

        else:  # Any other char that is not allowed for filename
            problem = ("({}'s not allowed)".format(letter))
        has_error = "yes"
        break

    if filename == "":  # makes sure filename isn't left empty
        problem = "can't be blank"
        has_error = "yes"

    if has_error == "yes":  # describe problem
        print("Invalid filename - {}".format(problem))
        print()
    else:
        print("You entered a valid filename")  # or allow a valid file name


# List of data type headers
Details = ['Question', 'Your Answer', 'Mark', 'Correct Answer']
with open(filename + ".csv", 'w', newline='') as f:
    write = csv.writer(f)
    write.writerow(Details)  # writes data type headers
    write.writerows(results)  # writes results
