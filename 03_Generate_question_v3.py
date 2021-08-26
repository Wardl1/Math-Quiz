"""Component 3 Generate_Questions version 2
this version fixes the negative answers for the subtraction questions and
fixes the question heading so that it keeps up to date with the question number
"""

from tkinter import *
from functools import partial  # To prevent unwanted additional windows
import random


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

    # math_addition function for when the addition_button is pressed
    def math_addition(self):
        print("1 + 1 = ")  # print statement to check function works
        QuestionGUI(self, quest_type="add").generate_question()  # opens question GUI

    # math_subtraction function for when the subtraction_button is pressed
    def math_subtraction(self):
        print("1 - 1 = ")  # print statement to check function works
        QuestionGUI(self, quest_type="sub").generate_question()  # opens question GUI

    # all_combined function for when the combined_button is pressed
    def all_combined(self):
        print("1 + / - 1 = ")  # print statement to check function works
        QuestionGUI(self, quest_type="both").generate_question()  # opens question GUI


class QuestionGUI:
    def __init__(self, partner, quest_type):
        # Formatting variables
        background_color = "#3399FF"  # darker blue
        # disable Main menu buttons
        partner.addition_button.config(state=DISABLED)
        partner.subtraction_button.config(state=DISABLED)
        partner.combined_button.config(state=DISABLED)

        # sets up question type to determine if its an add, sub or both question
        self.question_type = quest_type

        # sets up question answer which will be needed to evaluate if the user is correct
        self.question_answer = ""

        # sets up question number so that the question heading updates when next button is pressed
        self.question_number = 0

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
                                  command=partial(self.generate_question))
        self.next_button.grid(row=0, column=2)

    def generate_question(self):
        self.question_number += 1
        all_combined = ""  # all combined variable to switch between add and sub
        num_1 = random.randint(0, 10)  # generates random number
        num_2 = random.randint(0, 10)
        question = ""  # sets up question variable which is the text for the question_label
        if self.question_type == "both":
            all_combined = random.choice(["add", "sub"])  # chooses between add and sub to generate both questions
        if self.question_type == "add" or all_combined == "add":
            question = ("{} + {} = ".format(num_1, num_2))  # creates question
            self.question_answer = num_1 + num_2  # works out answer
        elif self.question_type == "sub" or all_combined == "sub":
            if num_1 > num_2:
                question = ("{} - {} = ".format(num_1, num_2))  # creates question
                self.question_answer = num_1 - num_2  # works out answer
            else:
                question = ("{} - {} = ".format(num_2, num_1))  # creates question
                self.question_answer = num_2 - num_1  # works out answer
        self.question_label.config(text=question)  # changes question label so that it is the
        self.question_heading_label.config(text="Question {}/10".format(self.question_number))



    def close_question(self, partner):
        # Put main menu button's back to normal...
        partner.addition_button.config(state=NORMAL)
        partner.subtraction_button.config(state=NORMAL)
        partner.combined_button.config(state=NORMAL)
        self.question_box.destroy()  # closes question GUI

    def enter_question(self):
        print("Wrong answer")  # prints to test button


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = MathQuiz()
    root.mainloop()
