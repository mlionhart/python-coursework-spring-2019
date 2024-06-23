# Module 5 - Skill Building Exercise No. 8 Solution
# Author: Bruce Elgort
# Date: July 22, 2017

def main():
    print("Average word length")
    print()

    # ask the user for a phrase (a sentence)
    phrase = input("Enter a phrase: ")

    # initialize variables
    count = 0
    theSum = 0

    # using accumulator loop
    # split the sentence into words and iterate through each word
    for word in phrase.split():
        theSum = theSum + len(word)
        # keep track of the number of words being processed
        count = count + 1

    # display results
    # take theSum and divide by number of words
    print("Average word length", theSum / count)

main()
