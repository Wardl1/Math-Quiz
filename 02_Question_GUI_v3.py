"""02 Question GUI version 3
continues on from Question GUI version 3
buttons on main menu are now disabled when the question GUI is opened
buttons are also enabled again when the Question GUI is closed
"""

from tkinter import *
from functools import partial  # To prevent unwanted additional windows


class MathQuiz:
    def __init__(self):
        # Formatting variables
        background_color = "#66FFFF"  # light blue

        # Main menu GUI frame
        self.main_menu_frame = Frame(width=300, height=300,
                                     bg=background_color, pady=10)
        self.main_menu_frame.grid()

        # Math Quiz heading (row 0)
        self.MathQuiz_label = Label(self.main_menu_frame,
                                    text="Math Quiz",
                                    font=("Arial", "16", "bold"),
                                    bg=background_color,
                                    padx=10, pady=10)
        self.MathQuiz_label.grid(row=0)

        # Simple instructions given
        self.intstruction_label = Label(self.main_menu_frame,
                                        text="Pick one area of math"
                                             " to work on \n and answer "
                                             "the 10 questions given.",
                                        font=("Arial", "12", "italic"),
                                        bg=background_color,
                                        padx=10, pady=10)
        self.intstruction_label.grid(row=1)

        # Addition button (row 2)
        self.addition_button = Button(self.main_menu_frame, text="Addition",
                                      font=("Arial", "14"),
                                      padx=10, pady=10,
                                      width=10,
                                      bg="#008CFF",  # darker blue
                                      fg="white",
                                      command=self.math_addition)
        self.addition_button.grid(row=2)

        # Subtraction button (row 3)
        self.subtraction_button = Button(self.main_menu_frame, text="Subtraction",
                                         font=("Arial", "14"),
                                         padx=10, pady=10,
                                         width=10,
                                         bg="#008CFF",  # darker blue
                                         fg="white",
                                         command=self.math_subtraction)
        self.subtraction_button.grid(row=3)

        # All combined button (row 4)
        self.combined_button = Button(self.main_menu_frame, text="All Combined",
                                      font=("Arial", "14"),
                                      padx=10, pady=10,
                                      width=10,
                                      bg="#008CFF",  # darker blue
                                      fg="white",
                                      command=self.all_combined)
        self.combined_button.grid(row=4)

    def math_addition(self):
        print("1 + 1 = ")  # print statement to check function works
        get_question = QuestionGUI(self)
        get_question.question_label.configure(text="1 + 1 = ")

    def math_subtraction(self):
        print("1 - 1 = ")  # print statement to check function works
        get_question = QuestionGUI(self)
        get_question.question_label.configure(text="1 - 1 = ")

    def all_combined(self):
        print("1 + / - 1 = ")  # print statement to check function works
        get_question = QuestionGUI(self)
        get_question.question_label.configure(text="1 + / - 1 = ")


class QuestionGUI:
    def __init__(self, partner):
        # Formatting variables
        background_color = "#3399FF"  # darker blue

        # disable Main menu buttons
        partner.addition_button.config(state=DISABLED)
        partner.subtraction_button.config(state=DISABLED)
        partner.combined_button.config(state=DISABLED)

        # sets up child window (ie: help box)
        self.question_box = Toplevel()

        # if users press at top, closes help and 'releases' help button
        self.question_box.protocol('WM_DELETE_WINDOW', partial(self.close_question,
                                                               partner))
        # Question Frame
        self.question_frame = Frame(self.question_box, width=300, bg=background_color)
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
        self.button_frame = Frame(self.question_box, width=300, bg=background_color)
        self.button_frame.grid(row=1)

        # Close button (row 0, column 0)
        self.close_button = Button(self.button_frame, text="Close",
                                   width=8, bg="light grey", font="arial 10 bold",
                                   command=partial(self.close_question, partner))
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

    def close_question(self, partner):
        # Put close button back to normal...
        partner.addition_button.config(state=NORMAL)
        partner.subtraction_button.config(state=NORMAL)
        partner.combined_button.config(state=NORMAL)
        self.question_box.destroy()

    def enter_question(self):
        print("Wrong answer")  # prints to test button

    def next_question(self):
        print("Next question")  # prints to test button


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = MathQuiz()
    root.mainloop()
