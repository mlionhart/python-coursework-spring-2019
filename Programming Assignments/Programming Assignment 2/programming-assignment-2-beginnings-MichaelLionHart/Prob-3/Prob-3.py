# Module 2
#   Programming Assignment 2
#     Prob-3.py

# YOUR NAME

def example():
    print("\nExample Output")

    # print a blank line
    print()

    # create three variables and assign three values in a single statement
    v1, v2, v3 = 21, 12.34, "hello"

    # print the variables
    print("v1:", v1)
    print("v2:", v2)
    print("v3:", v3)


def studentCode():
    # replace <name> with your name
    print("\nMike's Output")
    
    # print a blank line
    print()

    # replicate the assignment statement above, but use your own variable
    # names and values
    first, last, age = "Mike", "Hart", 32
    # print the values of the 3 variables
    print("First Name:", first)
    print("Last Name:", last)
    print("Age:", age)
    # Get 3 values from the user and assign them to the variables defined
    # above. See the page in Canvas on Simulataneous Assignment
    # BONUS POINTS for using the split() method
    first, last, age = input("Enter your first name, last name, and age (all separated by commas)").split()
    print("First Name:", first)
    print("Last Name:", last)
    print("Age:", age)
    print()

example()
studentCode()

