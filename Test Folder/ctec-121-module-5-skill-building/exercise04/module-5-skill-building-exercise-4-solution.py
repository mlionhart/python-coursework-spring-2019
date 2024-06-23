# Module 5 - Skill Building Exercise No. 4 Solution
# Author: Bruce Elgort
# Date: July 22, 2017

def main():
    print("This program builds acronyms")
    # get input from user
    phrase = input("Enter a phrase: ")
    # initialize variable to an empty string
    acronym = ""
    # split the sentence into a list of words
    # use a loop to iterate through the list of words
    for word in phrase.split():
        # concatenate the current value of acronym with the first
        # letter from the current word being iterated
        acronym = acronym + word[0]
    # convert the entire acroynum string to upper case
    acronym = acronym.upper()

    # display the acroynum
    print("The acronym is", acronym)

main()
