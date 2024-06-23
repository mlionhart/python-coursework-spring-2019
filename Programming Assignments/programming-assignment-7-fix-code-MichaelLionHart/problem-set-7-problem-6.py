# CTEC 121
# Author: Bruce Elgort
# problem-set-7-problem-6.py

"""
INSTRUCTIONS:

READ ALL OF THE INSTRUCTIONS BEFORE YOU START WORKING ON THE CODE

0) The code below will not run. Your job is to fix it.
1) The code below contains 5 errors.
2) Your job is to fix the errors and to place a comment above the line that
   contained the error and tell me what you fixed.
3) Make sure the code runs
"""

# Added open/close parentheses after 'main'
# erased space between 'main' and colon
def main():
    print("This program calculates the future value of an investment.")
    print()
    
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annualized interest rate: "))
    # Added closing parenthesis
    years = eval(input("Enter the number of years: "))

    print("Year   Value")
    print("------------")
    # Added colon at end of line
    for i in range(years+1):
        # use string formatting to make output align like sample provided
        # Added '$' before '{0:3}'
        # Added '}' after '${1:7.2f'
        print("${0:3}   ${1:7.2f}".format(i, principal))
        # Changed '==' operator to assignment operator ('=')
        principal = principal * (1 + apr)

main()

