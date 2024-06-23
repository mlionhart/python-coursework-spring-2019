# Module 6 - Problem Set No. 9 - Problem 1

"""
READ ALL INFORMATION CAREFULLY AND THEN READ IT AGAIN

IMPORTANT - PROVIDE AN IPO (Inputs, Processes, and Output) AT THE TOP OF 
EACH PROGRAM USING COMMENTS.

Write a program that gets a string containing the person's first, middle and 
last names using input(), and then displays their first, middle and last 
initials. For example, the user enters "Bruce Lawrence Elgort", the program 
should display B.L.E. It must display exactly like this with the .'s after 
each letter with no spaces.

IPO
==========
INPUTS:     input prompt for user's first, middle and last name, and setting it to variable 'name'

PROCESSES:  name = name.split();              # putting 'name' string into a list
            middle = name[1].capitalize()
            first = name[0].capitalize()      # creating separate name variables, using list indexing, 
            last = name[2].capitalize()       # and capitalizing the first letter in each string

OUTPUTS:    print(first[0] + '.' + middle[0] + '.' + last[0] + '.')     # using concatenation and string indexing to print the final initials, 
                                                                        # separated by periods
"""

def main():
    name = input('Please enter your first, middle and last name, separated by spaces (all in lowercase): ')
    name = name.split()
    first = name[0].capitalize()
    middle = name[1].capitalize()
    last = name[2].capitalize()
    print(first[0] + '.' + middle[0] + '.' + last[0] + '.')


main()