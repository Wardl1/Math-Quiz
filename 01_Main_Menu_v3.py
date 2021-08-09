"""Component 1 Main Menu GUI version 3
this version continues on from the last with all
buttons now in the GUI and all buttons have been formatted."""
from tkinter import *


class Math_quiz:
    def __init__(self):
        # Formatting variables
        background_color = "#66FFFF"  # light blue

        # Main menu GUI frame
        self.main_menu_frame = Frame(width=300, height=300,
                                     bg=background_color, pady=10)
        self.main_menu_frame.grid()

        # Math Quiz heading (row 0)
        self.math_quiz_label = Label(self.main_menu_frame,
                                     text="Math Quiz",
                                     font=("Arial", "16", "bold"),
                                     bg=background_color,
                                     padx=10, pady=10)
        self.math_quiz_label.grid(row=0)

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
                                      command=self.math_addition())
        self.addition_button.grid(row=2)

        # Subtraction button (row 3)
        self.subtraction_button = Button(self.main_menu_frame, text="Subtraction",
                                         font=("Arial", "14"),
                                         padx=10, pady=10,
                                         width=10,
                                         bg="#008CFF",  # darker blue
                                         fg="white",
                                         command=self.math_subtraction())
        self.subtraction_button.grid(row=3)

        # multiplication button (row 4)
        self.multiplication_button = Button(self.main_menu_frame, text="Multiplication",
                                            font=("Arial", "14"),
                                            padx=10, pady=10,
                                            width=10,
                                            bg="#008CFF",  # darker blue
                                            fg="white",
                                            command=self.math_multiplication())
        self.multiplication_button.grid(row=4)

        # Division button (row 5)
        self.division_button = Button(self.main_menu_frame, text="Division",
                                      font=("Arial", "14"),
                                      padx=10, pady=10,
                                      width=10,
                                      bg="#008CFF",  # darker blue
                                      fg="white",
                                      command=self.math_division())
        self.division_button.grid(row=5)

        # All combined button (row 6)
        self.combined_button = Button(self.main_menu_frame, text="All Combined",
                                      font=("Arial", "14"),
                                      padx=10, pady=10,
                                      width=10,
                                      bg="#008CFF",  # darker blue
                                      fg="white",
                                      command=self.all_combined())
        self.combined_button.grid(row=6)

    def math_addition(self):
        print("1 + 1 = ")  # print statement to check function works
        # get_addition = Addition()
        # get_addition.help_text.configure(text="1 + 1 = ")

    def math_subtraction(self):
        print("1 - 1 = ")  # print statement to check function works

    def math_multiplication(self):
        print("1 x 1 = ")  # print statement to check function works

    def math_division(self):
        print("1 / 1 = ")  # print statement to check function works

    def all_combined(self):
        print("1 + 1 = ")  # print statement to check function works


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Math_quiz()
    root.mainloop()
