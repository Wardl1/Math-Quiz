"""09 Warning GUI Version 1
sets up design for the Warning GUI
No buttons frame yet
"""

from tkinter import *


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


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = WarningGUI()
    root.mainloop()
