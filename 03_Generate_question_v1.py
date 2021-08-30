"""Component 3 Generate_Questions version 1
this version is not connected to the GUI's yet
"""

import random


def generate_question():
    all_combined = ""  # sets up all_combined variable
    question_answer = ""  # sets up question answer variable
    question = ""  # sets up question variable
    num_1 = random.randint(0, 10)  # generates a random number 1
    num_2 = random.randint(0, 10)  # generates a random number 2
    if question_type == "both":
        # randomly picks between add and sub so that it asks both when run
        all_combined = random.choice(["add", "sub"])
        # more than one round
    if question_type == "add" or all_combined == "add":
        question = ("{} + {} = ".format(num_1, num_2))  # Generates question
        question_answer = num_1 + num_2  # Works out answer
    elif question_type == "sub" or all_combined == "sub":
        # Generates sub question
        question = ("{} - {} = ".format(num_1, num_2))
        question_answer = num_1 - num_2  # works out answer
    print(question)  # prints question for testing
    print(question_answer)  # prints answer for testing


# Main routine for testing
question_type = "sub"  # sets question_type to "sub" for testing
generate_question()
question_type = "add"  # sets question_type to "add" for testing
generate_question()
question_type = "both"  # sets question_type to "both" for testing
generate_question()
generate_question()  # runs the function twice to see if it
# switches between add and sub correctly
