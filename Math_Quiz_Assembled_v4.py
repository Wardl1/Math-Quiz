"""10 Math Quiz Assembled version 4
warning GUI only appears if quiz is complete and close button is pressed
line 235 - only opens warning GUI if 10 questions are complete
"""

from tkinter import *
from functools import partial  # To prevent unwanted additional windows
import random
import csv
import re  # Imports the regular expression library re


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
        self.instruction_label = Label(self.main_menu_frame,
                                       text="Pick one area of math"
                                            " to work on \n and answer "
                                            "the 10 questions given.",
                                       font=("Arial", "12", "italic"),
                                       bg=background_color,
                                       padx=10, pady=10)
        self.instruction_label.grid(row=1)

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
        self.subtraction_button = Button(self.main_menu_frame,
                                         text="Subtraction",
                                         font=("Arial", "14"),
                                         padx=10, pady=10,
                                         width=10,
                                         bg="#008CFF",  # darker blue
                                         fg="white",
                                         command=self.math_subtraction)
        self.subtraction_button.grid(row=3)

        # All combined button (row 4)
        self.combined_button = Button(self.main_menu_frame,
                                      text="All Combined",
                                      font=("Arial", "14"),
                                      padx=10, pady=10,
                                      width=10,
                                      bg="#008CFF",  # darker blue
                                      fg="white",
                                      command=self.all_combined)
        self.combined_button.grid(row=4)

    # math_addition function for when the addition_button is pressed
    def math_addition(self):
        QuestionGUI(self, quest_type="add").generate_question()
        # opens question GUI

    # math_subtraction function for when the subtraction_button is pressed
    def math_subtraction(self):
        QuestionGUI(self, quest_type="sub").generate_question()
        # opens question GUI

    # all_combined function for when the combined_button is pressed
    def all_combined(self):
        QuestionGUI(self, quest_type="both").generate_question()
        # opens question GUI


class QuestionGUI:
    def __init__(self, partner, quest_type):
        # Formatting variables
        background_color = "#3399FF"  # darker blue
        # disable Main menu buttons
        partner.addition_button.config(state=DISABLED)
        partner.subtraction_button.config(state=DISABLED)
        partner.combined_button.config(state=DISABLED)

        # sets up results to record the results
        self.question_results = []

        # set up question so as to add to the results list
        self.question = ""

        # sets up question type to determine if its an add,
        # sub or both question
        self.question_type = quest_type

        # sets up question answer which will be needed to evaluate
        # if the user is correct
        self.question_answer = ""

        # sets up question number so that the question heading updates when
        # next button is pressed
        self.question_number = 0

        # sets up child window (ie: help box)
        self.question_box = Toplevel()

        # if users press at top, closes Question GUI
        # and enables Main Menu buttons
        self.question_box.protocol('WM_DELETE_WINDOW',
                                   partial(self.close_question, partner))

        # Question Frame
        self.question_frame = Frame(self.question_box, width=300,
                                    bg=background_color)
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
                                     pady=10, text="")
        self.evaluator_label.grid(row=3)

        # Sets up new frame for buttons to get a nice layout
        self.button_frame = Frame(self.question_box, width=300,
                                  bg=background_color)
        self.button_frame.grid(row=1)

        # Close button (row 0, column 0)
        self.close_button = Button(self.button_frame, text="Close",
                                   width=8, bg="light grey",
                                   font="arial 10 bold",
                                   command=partial(self.close_question,
                                                   partner))
        self.close_button.grid(row=0, column=0)

        # Enter button (row 0, column 1)
        self.enter_button = Button(self.button_frame, text="Enter",
                                   width=8, bg="light grey",
                                   font="arial 10 bold",
                                   command=partial(self.enter_question))
        self.enter_button.grid(row=0, column=1)

        # Next button (row 0, column 2)

        self.next_button = Button(self.button_frame, text="Next",
                                  width=8, bg="light grey",
                                  font="arial 10 bold",
                                  command=partial(self.generate_question),
                                  state=DISABLED)  # Starts as disabled
        self.next_button.grid(row=0, column=2)

        # Results Button remains Hidden until question 10/10
        # Same position as enter button as it appears where enter button was
        self.results_button = Button(self.button_frame, text="Results",
                                     width=8, bg="light grey",
                                     font="arial 10 bold",
                                     command=partial(self.go_to_results))
        self.results_button.grid_forget()

    def generate_question(self):
        # Return buttons and labels back to normal
        self.enter_button.config(state=NORMAL)  # Enables enter button so
        # that an answer can be entered
        self.answer_entry.config(bg="white")
        self.evaluator_label.config(text="")
        self.answer_entry.delete(0, END)

        # set up variables for generating question
        self.question_number += 1
        all_combined = ""  # all combined variable to switch between add/sub
        num_1 = random.randint(0, 10)  # generates random number
        num_2 = random.randint(0, 10)
        if self.question_type == "both":
            all_combined = random.choice(["add", "sub"])  # chooses between add
            # and sub to generate both questions
        if self.question_type == "add" or all_combined == "add":
            # creates question
            self.question = ("{} + {} = ".format(num_1, num_2))
            self.question_answer = num_1 + num_2  # works out answer
        elif self.question_type == "sub" or all_combined == "sub":
            if num_1 > num_2:
                # creates question
                self.question = ("{} - {} = ".format(num_1, num_2))
                self.question_answer = num_1 - num_2  # works out answer
            else:
                # creates question
                self.question = ("{} - {} = ".format(num_2, num_1))
                self.question_answer = num_2 - num_1  # works out answer
        self.question_label.config(text=self.question)  # updates question
        self.question_heading_label.config(text="Question {}/10".format(
            self.question_number))
        self.next_button.config(state=DISABLED)

    def close_question(self, partner):
        # Put main menu button's back to normal...
        partner.addition_button.config(state=NORMAL)
        partner.subtraction_button.config(state=NORMAL)
        partner.combined_button.config(state=NORMAL)
        self.question_box.destroy()  # closes question GUI
        if self.question_number == 10:
            WarningGUI(partner=self)  # opens warning GUI

    def enter_question(self):
        user_attempt = self.answer_entry.get()

        try:
            user_attempt = int(user_attempt)

            if user_attempt == self.question_answer:
                self.answer_entry.config(bg="green")
                self.evaluator_label.config(fg="green", text="Correct")
                right_or_wrong = "Correct"
            else:
                self.answer_entry.config(bg="red")
                self.evaluator_label.config(fg="red", text="Incorrect")
                right_or_wrong = "Incorrect"

            # Disable enter button so that they can't enter in another number
            self.enter_button.config(state=DISABLED)

            # Add question, user input and answer to results list
            # for results history
            self.question_results.append([self.question, user_attempt,
                                          right_or_wrong,
                                          self.question_answer])

            # Enable next button while the number of questions is under 10
            if self.question_number < 10:
                self.next_button.config(state=NORMAL)
            else:
                self.enter_button.grid_forget()  # enter button disappears
                # after 10 questions
                self.results_button.grid(row=0, column=1)  # results button
                # will appear after 10 questions

        except ValueError:
            self.evaluator_label.configure(text="Enter a number!!", fg="red")
            self.answer_entry.configure(bg="red")
            self.answer_entry.delete(0, END)

    def go_to_results(self):
        ResultsGUI(self, self.question_results)


class ResultsGUI:
    def __init__(self, partner, results_list):
        background = "white"

        # Disable Results button on Question GUI
        partner.results_button.config(state=DISABLED)

        # set up child window (ie: results box)
        self.results_box = Toplevel()

        # if users press at top, closes results GUI and enables results
        # button on Question GUI
        self.results_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_results, partner))

        # set up Heading Frame
        self.heading_frame = Frame(self.results_box,
                                   width=300, height=300, pady=10,
                                   bg=background)
        self.heading_frame.pack(side=TOP, fill=X)

        # Set up results heading (row 0)
        self.results_heading = Label(self.heading_frame, text="Results: ",
                                     font="arial 19 bold", bg=background)
        self.results_heading.grid(row=0)

        # set up results frame for the results to display in
        self.results_frame = Frame(self.heading_frame)
        self.results_frame.grid(row=1)

        # set up headings for result output
        # question number heading
        self.question_num = Label(self.results_frame, text="NO.",
                                  font="arial 18 italic")
        self.question_num.grid(row=0, column=0, padx=5)

        # quiz question heading
        self.quiz_question = Label(self.results_frame, text="Question:",
                                   font="arial 18 italic")
        self.quiz_question.grid(row=0, column=1, padx=5)

        # Your answer heading
        self.user_attempt = Label(self.results_frame, text="Your answer:",
                                  font="arial 18 italic")
        self.user_attempt.grid(row=0, column=2, padx=5)

        # Evaluation heading
        self.evaluation_heading = Label(self.results_frame, text="Mark:",
                                        font="arial 18 italic")
        self.evaluation_heading.grid(row=0, column=3, padx=5)

        # Correct answer heading
        self.answer_heading = Label(self.results_frame,
                                    text="Correct \nAnswer",
                                    font="arial 18 italic")
        self.answer_heading.grid(row=0, column=4, padx=5)

        row_num = 0  # row num variable so that it can change for each question
        for item in results_list:  # Each question
            col_num = 0  # sets column number to zero so that
            # each question is in the same column
            row_num += 1  # increases row so that
            # each question is on different row
            # sets question number e.g. 1)
            question_num = Label(self.results_frame, text=(row_num, ")"))
            question_num.grid(row=row_num, column=col_num)  # row=0, column=0
            for sub_item in item:  # question, user input,
                # evaluation and answer within the question
                col_num += 1  # increases column number so that
                # each item is displayed next to each other

                # displays the information for each question
                self.results_label = Label(self.results_frame, text=sub_item,
                                           font="Arial 12", justify=LEFT)
                self.results_label.grid(row=row_num, column=col_num, pady=5)

        # Export / Close buttons frame (row 2)
        self.button_frame = Frame(self.heading_frame)
        self.button_frame.grid(row=2, pady=10)

        # Export Button
        self.export_button = Button(self.button_frame, text="Export",
                                    font="arial 12 bold",
                                    command=partial(self.export_results,
                                                    partner))
        self.export_button.grid(row=0, column=0)

        # Close Button
        self.close_button = Button(self.button_frame, text="Close",
                                   font="arial 12 bold",
                                   command=partial(self.close_results,
                                                   partner))
        self.close_button.grid(row=0, column=1)

    # function to close Results GUI
    def close_results(self, partner):
        partner.results_button.config(
            state=NORMAL)  # re enables results button on Question GUI
        self.results_box.destroy()  # closes results GUI

    # function to open Export GUI
    def export_results(self, partner):
        ExportGUI(partner=self, results=partner.question_results,
                  from_warning=False)


class ExportGUI:
    def __init__(self, partner, results, from_warning):
        # Formatting variables
        background_color = "#CCFF99"  # light green

        self.export_results = results

        # Disables Export button on Results GUI
        partner.export_button.config(state=DISABLED)

        # if export GUI is opened from Warning GUI then warning GUI will close
        if from_warning:
            partner.warning_box.destroy()

        # set up child window (ie: export box)
        self.export_box = Toplevel()

        # if users presses close at top, closes Export GUI and enables export
        # button on Results GUI
        self.export_box.protocol('WM_DELETE_WINDOW',
                                 partial(self.cancel_export, partner,
                                         from_warning=from_warning))

        # Export Frame
        self.export_frame = Frame(self.export_box, width=300,
                                  bg=background_color)
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
                                    command=partial(self.cancel_export,
                                                    partner,
                                                    from_warning=from_warning))
        self.cancel_button.grid(row=0, column=0, padx=15)

        # Save button (row 0, column 1)
        self.save_button = Button(self.button_frame, text="Save",
                                  width=8, bg="light grey",
                                  font="arial 10 bold",
                                  command=partial(self.save_results, partner,
                                                  from_warning=from_warning))
        self.save_button.grid(row=0, column=1, padx=15)

    def cancel_export(self, partner, from_warning):
        self.export_box.destroy()  # closes export GUI
        if not from_warning:  # only enables export button
            # if export GUI is opened from Results GUI
            partner.export_button.config(state=NORMAL)

    def save_results(self, partner, from_warning):
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
                break
            else:
                # List of data type headers
                details = ['Question', 'Your Answer', 'Mark', 'Correct Answer']
                with open(filename + ".csv", 'w', newline='') as f:
                    write = csv.writer(f)
                    write.writerow(details)  # writes data type headers
                    write.writerows(self.export_results)  # writes results
                    self.export_box.destroy()  # closes export GUI
                    if not from_warning:
                        # re enables export button on Results GUI
                        partner.export_button.config(state=NORMAL)


class WarningGUI:
    def __init__(self, partner):
        # Formatting variables
        background_color = "#FF9999"  # light red

        # set up child window (ie: warning box)
        self.warning_box = Toplevel()

        # Warning Frame
        self.warning_frame = Frame(self.warning_box,
                                   width=300, bg=background_color)
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
                                    command=partial(self.open_export,
                                                    partner))
        self.export_button.grid(row=0, column=1, padx=15)

    def close_warning(self):
        self.warning_box.destroy()

    def open_export(self, partner):
        ExportGUI(self, results=partner.question_results, from_warning=True)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = MathQuiz()
    root.mainloop()
