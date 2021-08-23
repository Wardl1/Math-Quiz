"""02 Question GUI version 1
Set up design for question GUI
No Main Menu GUI connected yet
close button doesnt work yet
all buttons print a statement to test if they work
"""

from tkinter import *
from functools import partial  # To prevent unwanted additional windows


class QuestionGUI:
    def __init__(self):
        # Formatting variables
        background_color = "#3399FF"  # darker blue

        # Question Frame
        self.question_frame = Frame(width=300, bg=background_color)
        self.question_frame.grid()

        # Question Heading (row 0)
        self.question_heading_label = Label(self.question_frame,
                                            text="Question 1/10",
                                            font="Arial 16 bold",
                                            bg=background_color,
                                            padx=10, pady=10)
        self.question_heading_label.grid(row=0)

        # User question to answer (row 1)
        self.question_label = Label(self.question_frame,
                                    text="1 + 1 = ",
                                    font="Arial 12 bold", wrap=250,
                                    justify=CENTER, bg=background_color,
                                    padx=10, pady=10)
        self.question_label.grid(row=1)

        # Answer entry box (row 2)
        self.answer_entry = Entry(self.question_frame, width=20,
                                  font="Arial 14 bold",
                                  bg="white")
        self.answer_entry.grid(row=2)

        # Incorrect or correct statement (row 3)
        self.evaluator_label = Label(self.question_frame,
                                     font="Arial 14 bold",
                                     fg="green",
                                     bg=background_color,
                                     pady=10, text="Correct")
        self.evaluator_label.grid(row=3)

        # Sets up new frame for buttons to get a nice layout
        self.button_frame = Frame(width=300, bg=background_color)
        self.button_frame.grid(row=1)

        # Close button (row 0, column 0)
        self.close_button = Button(self.button_frame, text="Close",
                                   width=8, bg="light grey", font="arial 10 bold",
                                   command=partial(self.close_question))
        self.close_button.grid(row=0, column=0)

        # Enter button (row 0, column 1)
        self.enter_button = Button(self.button_frame, text="Enter",
                                   width=8, bg="light grey", font="arial 10 bold",
                                   command=partial(self.enter_question))
        self.enter_button.grid(row=0, column=1)

        # Next button (row 0, column 2)
        self.next_button = Button(self.button_frame, text="Next",
                                  width=8, bg="light grey", font="arial 10 bold",
                                  command=partial(self.next_question))
        self.next_button.grid(row=0, column=2)

    def close_question(self):
        print("You wish to close the question")  # prints to test button

    def enter_question(self):
        print("Wrong answer")  # prints to test button

    def next_question(self):
        print("Next question")  # prints to test button


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = QuestionGUI()
    root.mainloop()
