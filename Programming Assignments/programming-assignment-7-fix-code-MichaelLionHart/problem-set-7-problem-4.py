# CTEC 121
# Author: Bruce Elgort
# problem-set-7-problem-4.py

"""
INSTRUCTIONS:

READ ALL OF THE INSTRUCTIONS BEFORE YOU START WORKING ON THE CODE

0) The code below will not run. Your job is to fix it.
1) The code below contains 4 errors.
2) Your job is to fix the errors and to place a comment above the line that
   contained the error and tell me what you fixed.
3) Make sure the code runs
"""

"""
An acronym is a word formed by taking the first letters of the words in a 
phrase and making a word from them. For example, RAM is an acronym for 
“random access memory.” Write a program that allows the user to type in a 
phrase and then outputs the acronym for that phrase. Note: the acronym 
should be all uppercase, even if the words in the phrase are not capitalized.
"""

def main():
    # Erased extra paren
    print("This program builds acronyms")
    # get input from user
    # Erased extra paren
    phrase = input("Enter a phrase: ")
    # initialize variable to an empty string
    # Changed quotes so they match
    acronym = ''
    # split the sentence into a list of words
    # use a loop to iterate through the list of words
    # Added colon at the end of this line
    for word in phrase.split():
        # concatenate the current value of acronym with the first
        # letter from the current word being iterated
        acronym = acronym + word[0]
    # convert the entire acroynum string to upper case
    acronym = acronym.upper()

    # display the acroynum
    print("The acronym is", acronym)

main()


