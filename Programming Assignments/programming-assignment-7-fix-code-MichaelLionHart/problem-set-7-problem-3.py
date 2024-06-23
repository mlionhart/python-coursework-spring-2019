# CTEC 121
# Author: Bruce Elgort
# problem-set-7-problem-3.py

"""
INSTRUCTIONS:

READ ALL OF THE INSTRUCTIONS BEFORE YOU START WORKING ON THE CODE

0) The code below will not run. Your job is to fix it.
1) The code below contains 5 errors.
2) Your job is to fix the errors and to place a comment above the line that
   contained the error and tell me what you fixed.
3) Make sure the code runs
"""


def main():
    print("Exam Grader")
    score = eval(input("Enter the score (out of 100): "))
    # create a single string of all the letters
    # Erased 'x' and added '+' before '11x"A"'
    # Changed all instances of 'x' (besides the one mentioned in the comment above), to the '*' operator. 
    # Added parentheses around every expression in the form (number * "letter")
    grades = (60 * "F") + (10 * "D") + (10 * "C") + (10 * "B") + (11 * "A")
    # uncomment the line below to see how this works
    print(grades)

    # display result
    print("The grade is", grades[score])

main()

