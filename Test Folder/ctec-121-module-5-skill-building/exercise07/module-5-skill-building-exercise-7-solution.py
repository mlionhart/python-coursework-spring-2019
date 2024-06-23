# Module 5 - Skill Building Exercise No. 7 Solution
# Author: Bruce Elgort
# Date: July 22, 2017

def main():
    print("Caesar cipher")
    print()
    # get the numberic key value from the user
    key = eval(input("Enter the key value: "))
    # enter the phrase to encode
    plain = input("Enter the phrase to encode: ")
    # initialize cipher variable to an empty string
    cipher = ""
    # iterate through each character of the phrase one letter at a time
    for letter in plain:
        # use accumulator pattern
        # encode letter and use the key to shift it's value
        cipher = cipher + chr(ord(letter) + key)

    # display the encoded message
    print("Encoded message follows:")
    print(cipher)

main()
