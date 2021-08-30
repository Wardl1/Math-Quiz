"""Component 06 Results GUI trial 1 version 1
Sets up design for the results GUI
this trials setting the information as a table like display
each item in each item in the list is given a new column and
each item/question is given a new row
close and export buttons do not work yet
Results GUI is not connected to the other GUI's yet
"""

from tkinter import *

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

        # set up Heading Frame
        self.heading_frame = Frame(width=300, height=300, pady=10,
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
            for sub_item in item:  # question, user input, evaluation
                # and answer within the question
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
