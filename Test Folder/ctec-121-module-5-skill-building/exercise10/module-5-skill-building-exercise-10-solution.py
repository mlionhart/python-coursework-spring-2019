# Module 5 - Skill Building Exercise No. 10 Solution
# Author: Bruce Elgort
# Date: July 22, 2017

def main():
    print("File wordcount")
    print()
    # ask for file name. Use skill_building_29_text.txt
    fname = input("Enter filename: ")
    # open the file in read mode
    infile = open(fname, 'r')
    # read the contents of the entire file
    chars = infile.read()
    # clse the file
    infile.close()
    # split the contents by the default space character
    words = chars.split()
    # split the contents by the new line character
    lines = chars.split("\n")
    # display the results by using the len() function
    print("Characters:", len(chars))
    print("Words:", len(words))
    print("Lines:", len(lines))

main()
