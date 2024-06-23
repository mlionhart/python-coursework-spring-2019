# CTEC 121
# Author: Bruce Elgort
# problem-set-7-problem-2.py

'''
INSTRUCTIONS:

READ ALL OF THE INSTRUCTIONS BEFORE YOU START WORKING ON THE CODE

0) The code below will not run. Your job is to fix it.
1) The code below contains 2 errors.
2) Your job is to fix the errors and to place a comment above the line that
   contained the error and tell me what you fixed.
3) Make sure the code runs
'''

def main():
    print("Five point quiz grader")
    # ask for user input
    # Changed 'iput' to 'input'
    score = eval(input("Enter the score: "))
    # locate position within the string
    # Moved end quote - placing it in its correct position (after the string)
    grade = "FFDCBA"[score]
    # display result
    print("The grade is", grade)

main()

