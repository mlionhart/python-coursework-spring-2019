# Module 4
#   Programming Assignment 5
#       Prob-1.py

# Mike Hart

# Inputs: Number input by user
# Processing: if-elif-else statement - converting number to romanNumeral
# Outputs:  Print statements in all functions


def unitTest():
    print("\nUnit Tests")
    for x in range(1,11,1):
        print("Input number", x, "translates to", converter(x), "in Roman Numerals")
        


def converter(number):
    error = "Incorrect number"
    if number == 1:
        romanNumeral = 'I'
    elif number == 2:
        romanNumeral = 'II'
    elif number == 3:
        romanNumeral = 'III'
    elif number == 4:
        romanNumeral = 'IV'
    elif number == 5:
        romanNumeral = 'V'
    elif number == 6:
        romanNumeral = 'VI'
    elif number == 7:
        romanNumeral = 'VII'
    elif number == 8:
        romanNumeral = 'VIII'
    elif number == 9:
        romanNumeral = 'IX'
    elif number == 10:
        romanNumeral = 'X'
    else:
        romanNumeral = error

    return romanNumeral 
    print("Input number", number, "translates to", romanNumeral, "in Roman Numerals")


def main():
    number = eval(input('Enter a number between 1 and 10: '))
    print("Input number", number, "translates to", converter(number), "in Roman Numerals")

main()
unitTest()