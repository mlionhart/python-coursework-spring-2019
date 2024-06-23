# Module 2
#   Programming Assignment 3
#     Prob-2.py

# Mike Hart

def example():
    print("\nExample Output")
   # section 1
    x = 5
    # print x and its type
    print("x", x, "is a", type(x))

    # section 2
    print()
    x = float(x)
    print("x", x, "is a", type(x))

def studentCode():
    print("\nStudent Output")
    # section 1
    x = 5
    y = 3.14
    z = "a string"

    # print the values for x, y, and z and their types each on a separate line
    print((x), type(x))
    print((y), type(y))
    print((z), type(z))

    print()
    # section 2
    # convert y to an int and print
    y = 9.99
    print(int(y))
    print()

    # convert y to an int and print

    z = "12.34"
    # print z and its type
    print((z), type(z))
    print()
    
    # use eval() to convert z to a number and print its value and type
    z = eval(z)
    print((z), type(z))

    print()

example()
studentCode()