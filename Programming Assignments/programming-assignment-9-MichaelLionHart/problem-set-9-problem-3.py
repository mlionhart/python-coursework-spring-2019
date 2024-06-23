# Module 6 - Problem Set No. 9 - Problem 3

"""
READ ALL INFORMATION CAREFULLY AND THEN READ IT AGAIN

IMPORTANT - PROVIDE AN IPO (Inputs, Processes, and Output) AT THE TOP OF 
EACH PROGRAM USING COMMENTS.

Write a program that asks the user to enter a series of single-digit numbers 
with nothing separating them. Use input() for this since we want to have a 
string of numbers. The program should display the sum of all the single digit 
numbers in the string. For example, if the user enters 2514, the method 
should return 12, which is the sum of 2, 5, 1 and 4. You can use input() to 
get the numbers as a string and then use Python coding to convert them to 
numbers as needed.

HINTS
========================
- Iterate through each character in the string using a loop. See video in 
  Canvas.
- Use a loop and use range(len(theString)) for your loop
- Remember that as you iterate through the loop, the iterator value can be 
  used to slice into the string
- Convert the string to a numeric value using int()
- Use the accumulator pattern to sum the numbers. See video in Canvas.

IPO
==========
INPUTS:     numbers = input('enter a series of numbers: ')  # having user input numbers, then assigning them to variable
            digit = ''                                      # creating empty string to store values to be converted to int
            finalDigit = 0                                  # creating variable to accumulate the sum of each integer

PROCESSES:  for number in range(len(numbers)):              # for loop to iterate through the numbers string
                digit = numbers[number]                     # selecting next character in numbers string by string indexing
                digit = int(digit)                          # converting character to an integer
                finalDigit = finalDigit + digit             # accumulating the final sum through each iteration of the loop

OUTPUTS:    print()
            print('The sum of the numbers you entered is: ', finalDigit)     # printing output
            print()

"""

def main():
    numbers = input('enter a series of numbers: ')
    digit = ''
    finalDigit = 0
    for number in range(len(numbers)):
        digit = numbers[number]
        digit = int(digit)
        finalDigit = finalDigit + digit
    print()
    print('The sum of the numbers you entered is: ', finalDigit)
    print()

main()