# Module 5 - Skill Building Exercise No. 5 Solution
# Author: Bruce Elgort
# Date: July 22, 2017

def main():
    print("This program computes the 'number value' of a name")
    print()

    # Ask for a persons name
    name = input("Enter a single name: ")
    # set variable to 0
    # we will use it to accumulate the sum of the values of the numbers
    theSum = 0
    for letter in name:
        # conver the letter to lower case and then use ord to get it's value
        # do the same with the lower case 'a' and then add 1
        theSum = theSum + ord(letter.lower()) - ord('a') + 1

    # display the sum
    print("The value is:", theSum)

main()
