"""Component 07 Export Results trial 1 version 1
the user inputs a filename (assume valid data)
non valid input for filename will be dealt with in later versions
this trial converts all items in the results list to a string
then exports each item to a .txt file
"""


# list of results for export (for testing)
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
filename += ".txt"  # add .txt suffix to the filename

# Create file to hold data
f = open(filename, "w+")
# new list to hold only string values from results list
results_list_str = []

for item in results:
    # list to hold each question as a string before they are appended
    sub_results_list = []
    for sub_item in item:  # each part of each question
        # e.g. user input, question
        if isinstance(sub_item, int):  # if sub_item is an integer
            sub_item_str = str(sub_item)  # converts to string
            # appends sub_item to the sub_results_list
            sub_results_list.append(sub_item_str)
        else:  # if sub_item is not an integer
            sub_results_list.append(sub_item)
    results_list_str.append(sub_results_list)

for question in results_list_str:  # each question
    for data_type in question:  # each data type withing each question
        # each data type within one question being exported
        f.write(data_type + ", ")
    f.write("\n")  # new line for each question
# close file
f.close()
