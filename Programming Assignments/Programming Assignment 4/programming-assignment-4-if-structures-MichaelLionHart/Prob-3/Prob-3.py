# Module 3
#   Programming Assignment 4
#     Prob-3.py

# Mike Hart

def letterGrade(score):
    if score == 0:
        letterGrade = 'F'
    elif score == 1:
        letterGrade = 'F'
    elif score == 2:
        letterGrade = 'D'
    elif score == 3:
        letterGrade = 'C'
    elif score == 4:
        letterGrade = 'B'
    else:
        letterGrade = 'A'

    return letterGrade

def unitTest():
    for score in range(6):
        print("Letter Grade if score == ", score, ":\t", letterGrade(score))
    
   

if __name__ == "__main__":
    unitTest()