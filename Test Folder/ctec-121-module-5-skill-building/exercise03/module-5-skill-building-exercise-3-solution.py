# Module 5 - Skill Building Exercise No. 3 Solution
# Author: Bruce Elgort
# Date: July 22, 2017

def main():
    print("Exam Grader")
    score = eval(input("Enter the score (out of 100): "))
    # create a single string of all the letters
    grades = 60*"F"+10*"D"+10*"C"+10*"B"+11*"A"
    # uncomment the line below to see how this works
    #print(grades)

    # display result
    print("The grade is", grades[score])

main()
