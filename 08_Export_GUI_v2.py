"""08 Export GUI version 2
Continues on from version 1 but now adds the 07_Export_Results component
No Main Menu GUI connected yet
Save button now works to export results to a .csv file
close button still doesn't work
"""

from tkinter import *
from functools import partial  # To prevent unwanted additional windows
import csv
import re  # Imports the regular expression library re


class ExportGUI:
    def __init__(self):
        # Formatting variables
        background_color = "#CCFF99"  # light green

        # Export Frame
        self.export_frame = Frame(width=300, bg=background_color)
        self.export_frame.pack(side=TOP, fill=X)

        # Export Heading (row 0)
        self.export_heading_label = Label(self.export_frame,
                                          text="Export",
                                          font="Arial 18 bold",
                                          bg=background_color,
                                          padx=10, pady=10)
        self.export_heading_label.grid(row=0)

        # Export label with instructions (row 1)
        self.export_label = Label(self.export_frame,
                                  text="Please enter the desired filename "
                                       "below. Your Math results will be "
                                       "exported as .csv file and will "
                                       "appear in the same folder as this "
                                       "program.",
                                  font="Arial 12 bold", wrap=250,
                                  justify=CENTER, bg=background_color,
                                  padx=10, pady=10)
        self.export_label.grid(row=1)

        # Filename entry box (row 2)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold",
                                    bg="white")
        self.filename_entry.grid(row=2)

        # Problem with filename statement (row 3)
        self.problem_label = Label(self.export_frame,
                                   font="Arial 14 bold",
                                   fg="red",
                                   bg=background_color,
                                   pady=5, text="")
        self.problem_label.grid(row=3)

        # Sets up new frame for buttons to get a nice layout
        # Export / Close buttons frame (row 4)
        self.button_frame = Frame(self.export_frame, bg=background_color)
        self.button_frame.grid(row=4, pady=10)

        # Close button (row 0, column 0)
        self.cancel_button = Button(self.button_frame, text="Cancel",
                                    width=8, bg="light grey",
                                    font="arial 10 bold",
                                    command=partial(self.cancel_export))
        self.cancel_button.grid(row=0, column=0, padx=15)

        # Save button (row 0, column 1)
        self.save_button = Button(self.button_frame, text="Save",
                                  width=8, bg="light grey",
                                  font="arial 10 bold",
                                  command=partial(self.save_results))
        self.save_button.grid(row=0, column=1, padx=15)

    def cancel_export(self):
        print("You wish to close Export GUI")  # prints to test button

    def save_results(self):
        # Get filename, can't be blank / invalid
        has_error = "yes"
        while has_error == "yes":
            problem = ""
            has_error = "no"
            filename = self.filename_entry.get()
            # Regular expression to check file name
            # Can be Upper or lower case letters, numbers or underscores
            valid_char = "[A-Za-z0-9_]"
            for letter in filename:
                if re.match(valid_char, letter):
                    continue  # If the letter is valid,
                    # goes back and checks the next

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
                self.problem_label.config(
                    text="Invalid filename - {}".format(problem))
                self.filename_entry.delete(0, END)  # clears filename entry
                print()
                break
            else:
                print(
                    "You entered a valid filename")
                # List of data type headers
                details = ['Question', 'Your Answer', 'Mark', 'Correct Answer']
                with open(filename + ".csv", 'w', newline='') as f:
                    write = csv.writer(f)
                    write.writerow(details)  # writes data type headers
                    write.writerows(results)  # writes results


# list of results for export (just used for testing)
results = ['5 + 1 = ', 6, 'Correct', 6], ['1 + 2 = ', 3, 'Correct', 3], \
          ['0 + 5 = ', 5, 'Correct', 5], \
          ['5 + 0 = ', 5, 'Correct', 5], ['10 + 10 = ', 20, 'Correct', 20], \
          ['5 + 3 = ', 8, 'Correct', 8], \
          ['6 + 10 = ', 16, 'Correct', 16], ['4 + 7 = ', 11, 'Correct', 11], \
          ['2 + 8 = ', 10, 'Correct', 10], \
          ['2 + 3 = ', 5, 'Correct', 5]

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = ExportGUI()
    root.mainloop()
