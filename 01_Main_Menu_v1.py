"""Component 1 Main Menu GUI version 1
this version just has the heading and a small set of instructions
no buttons have been created yet"""

from tkinter import *


class Math:
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


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Math()
    root.mainloop()
