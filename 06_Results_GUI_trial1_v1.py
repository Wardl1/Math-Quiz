"""Component 06 Results GUI trial 1 version 1
Sets up design for the results GUI
This trials putting all the items in the list into one long string
this string is then the text for a label on the GUI which displays
the information
integer items in the results list have to be converted into a string item
each question is on a new line within the results string
close and export buttons do not work yet
Results GUI is not connected to the other GUI's yet
"""

from tkinter import *

# list of results for testing
results = ['5 + 1 = ', 6, 'Correct', 6], ['1 + 2 = ', 3, 'Correct', 3], \
          ['0 + 5 = ', 5, 'Correct', 5], \
          ['5 + 0 = ', 5, 'Correct', 5], ['10 + 10 = ', 20, 'Correct', 20], \
          ['5 + 3 = ', 8, 'Correct', 8], \
          ['6 + 10 = ', 16, 'Correct', 16], ['4 + 7 = ', 11, 'Correct', 11], \
          ['2 + 8 = ', 10, 'Correct', 10], \
          ['2 + 3 = ', 5, 'Correct', 5]


class ResultsGUI:
    def __init__(self, results_list):
        background = "white"

        # Disable Results button on Question GUI

        # set up child window (ie: results box)

        # if users press at top, closes results and enables results button

        # set up GUI Frame
        self.history_frame = Frame(width=300, height=300, pady=10,
                                   bg=background)
        self.history_frame.grid()

        # Set up results heading (row 0)
        self.results_heading = Label(self.history_frame, text="Results: ",
                                     font="arial 19 bold", bg=background)
        self.results_heading.grid(row=0)

        # Add items of the list to the results string
        results_string = ""
        for item in results_list:  # each question
            for sub_item in item:  # each part of each question
                # e.g. user input, question
                if isinstance(sub_item, int):  # if sub_item is an integer
                    sub_item_str = str(sub_item)  # converts to string
                    # adds sub_item to the results string
                    results_string += sub_item_str
                else:  # if sub_item is not an integer
                    results_string += sub_item  # add it to the results string
                results_string += " "  # add a space between each item
            results_string += "\n"  # new line for each question

        # Label to display the question results
        # text is the results string which was created from the results list
        self.results_label = Label(self.history_frame, text=results_string,
                                   bg=background, font="Arial 12",
                                   justify=LEFT)
        self.results_label.grid(row=1)

        # Export / Close buttons frame (row 2)
        self.button_frame = Frame(self.history_frame)
        self.button_frame.grid(row=2, pady=10)

        # Export Button
        self.export_button = Button(self.button_frame, text="Export",
                                    font="arial 12 bold",
                                    command=self.export_results)
        self.export_button.grid(row=0, column=0)

        # Close Button
        self.close_button = Button(self.button_frame, text="Close",
                                   font="arial 12 bold",
                                   command=self.close_results)
        self.close_button.grid(row=0, column=1)

    # function to close Results GUI
    def close_results(self):
        print("Close")

    # function to open Export GUI
    def export_results(self):
        print("Export")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = ResultsGUI(results)
    root.mainloop()
