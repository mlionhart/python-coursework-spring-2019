# Module 7
#   Programming Assignment 10
#     Prob-1.py

# Mike Hart


def main():
    sum = 0.0
    x = float(input("Enter a number (negative to quit) >> "))
    while x >= 0:
        sum = sum + x
        x = float(input("Enter a number (negative to quit) >> "))
    print("\nThe sum of the numbers is", sum)


main()    