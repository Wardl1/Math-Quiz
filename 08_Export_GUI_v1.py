"""08 Export GUI version 1
Set up design for Export GUI
No Main Menu GUI connected yet
close and save buttons don't work yet
Does not export to .csv file
"""

from tkinter import *
from functools import partial  # To prevent unwanted additional windows


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
        self.close_button = Button(self.button_frame, text="Close",
                                   width=8, bg="light grey",
                                   font="arial 10 bold",
                                   command=partial(self.close_export))
        self.close_button.grid(row=0, column=0, padx=15)

        # Save button (row 0, column 1)
        self.save_button = Button(self.button_frame, text="Save",
                                  width=8, bg="light grey",
                                  font="arial 10 bold",
                                  command=partial(self.save_results))
        self.save_button.grid(row=0, column=1, padx=15)

    def close_export(self):
        print("You wish to close Export GUI")  # prints to test button

    def save_results(self):
        print("Save results")  # prints to test button


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = ExportGUI()
    root.mainloop()
