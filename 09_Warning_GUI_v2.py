"""09 Warning GUI Version 2
Buttons frame is set up now
full design is complete
buttons do not work yet and just print a statement
"""

from tkinter import *
from functools import partial  # To prevent unwanted additional windows


class WarningGUI:
    def __init__(self):
        # Formatting variables
        background_color = "#FF9999"  # light red

        # Warning Frame
        self.warning_frame = Frame(width=300, bg=background_color)
        self.warning_frame.pack(side=TOP, fill=X)

        # Warning Heading (row 0)
        self.warning_heading_label = Label(self.warning_frame,
                                           text="Warning:",
                                           font="Arial 18 bold",
                                           bg=background_color,
                                           padx=10, pady=10)
        self.warning_heading_label.grid(row=0)

        # warning label with message (row 1)
        self.warning_label = Label(self.warning_frame,
                                   text="If you close the quiz without "
                                        "exporting the results, all results "
                                        "and evidence from the quiz will be "
                                        "lost. To save a record of your "
                                        "results please press Export.",
                                   font="Arial 12 bold", wrap=250,
                                   justify=CENTER, bg=background_color,
                                   padx=10, pady=10)
        self.warning_label.grid(row=1)

        # Sets up new frame for buttons to get a nice layout
        # buttons frame (row 2)
        self.button_frame = Frame(self.warning_frame, bg=background_color)
        self.button_frame.grid(row=2, pady=10)

        # Close button (row 0, column 0)
        self.close_button = Button(self.button_frame, text="Close",
                                   width=8, bg="light grey",
                                   font="arial 10 bold",
                                   command=partial(self.close_warning))
        self.close_button.grid(row=0, column=0, padx=15)

        # Export button (row 0, column 1)
        self.export_button = Button(self.button_frame, text="Export",
                                    width=8, bg="light grey",
                                    font="arial 10 bold",
                                    command=partial(self.open_export))
        self.export_button.grid(row=0, column=1, padx=15)

    def close_warning(self):
        print("You wish to close Warning GUI")  # prints to test button

    def open_export(self):
        print("Export GUI")  # prints to test button


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = WarningGUI()
    root.mainloop()
