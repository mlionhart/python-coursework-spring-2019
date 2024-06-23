# Module 5 - Skill Building Exercise No. 2 Solution
# Author: Bruce Elgort
# Date: July 22, 2017

def main():
    print("Five point quiz grader")
    # ask for user input
    score = eval(input("Enter the score: "))
    # locate position within the string
    grade = "FFDCBA"[score]
    # display result
    print("The grade is", grade)

main()
