# Module 5 - Skill Building Exercise No. 6 Solution
# Author: Bruce Elgort
# Date: July 22, 2017

def main():
    print("This program computes the 'number value' of a name")
    print()

    # get a name (multiple words)
    names = input("Enter a name: ")

    # Create a string of all the letters -- avoids nested loop
    letters = "".join(names.split())
    # initialize variable theSum to 0
    theSum = 0
    for letter in letters:
        theSum = theSum + ord(letter.lower()) - ord('a') + 1

    # display the result
    print("The value is:", theSum)

main()
