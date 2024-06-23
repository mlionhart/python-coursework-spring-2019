# Module 2
#   Programming Assignment 3
#     Prob-4.py

# Mike Hart

def main():
    print("\nStudent Output")

    # write code that will sum the numbers between 15 and 30 inclusive
    # and print the sum
    sum = 0
    for i in range(15,31):
        sum = sum + i
    print(sum)
    print()

    # sum the numbers in the sequence [2, 4, 7, 9, 12, 14, 17, 19]
    # and print the sum
    sum = 0
    for i in [2,4,7,9,12,14,17,19]:
        sum = sum + i
    print(sum)
    print()

    # use the randrange() function to sum 5 randomly generated numbers 
    # between 1 and 99 inclusive.
    # Print each random number on a line. 
    # Print the sum on the last line
    import random
    a = random.randrange(1,99)
    b = random.randrange(1,99)
    c = random.randrange(1,99)
    d = random.randrange(1,99)
    e = random.randrange(1,99)
    
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

    sum = 0
    for i in [a,b,c,d,e]:
        sum = sum + i
    print("sum = ",sum)


main()
