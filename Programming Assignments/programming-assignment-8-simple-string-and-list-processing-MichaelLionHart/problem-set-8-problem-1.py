# Module 5 - Problem Set No. 8 Problem 1

# INSTRUCTIONS

# Add a comment above each line of code describing what it does.
# Be specific. Use multiple comment lines if you need to
# OR write code below the comments requesting code.
# Make sure your file runs and generates the correct results.

def main():
    # define variable str1 with string "Hello"
    str1 = "Hello"
    #print out the 2nd letter
    print(str1[1])

    # ASSIGNMENT QUESTIONS START HERE
    # prints the second-to-last character in str1
    print(str1[-2])
    # prints the first three characters of str1
    print(str1[:3])
    # prints from character 3 through character 5 (not including 5) - which yield 'll'
    print(str1[2:len(str1)-1])
    # creating variable named str2 and setting its value to 'World'
    str2 = "World"
    # printing str1 and str2 concatenated together
    print(str1+str2)

    # write code below to iterate over str1 and print each character
    # separated by a space in a single line
    for i in range(len(str1)):
        print(str1[i], end=' ')

    # write code below. Create 2 lists. Print each. Print concatenation of them.
    print()
    list1 = ['michael', 'ryan', 'hart']
    list2 = ['daniel', 'james', 'hart']
    print()
    
    # write code that demonstrates you can append to list1 created above
    list1.append('is awesome')
    print(list1)
    print()
    
    # write code that demonstrates parsing of an input phrase into words in a list'
    phrase = input('Enter a phrase: ')
    print(phrase.split())
    print()

    # write code that gets pi from the math library and outputs as "3.14"
    # using string formatting.
    import math
    print('the value of pi is {0:0.2f}'.format(math.pi))

    # in the code below, what does line[:-1] evaluate to?
    # assume infile has been opened for reading a text file
    # assume infile is a text file with multiple lines each line ending with
    # a carriage return/linefeed character
    # NOTE: you are just being asked to answer the questions above. DO NOT
    # uncomment the code below.
    '''
    for line in infile:
        # [:-1] means every character in the string of the line, except the last character (which is the newline character - which is the purpose of this code)
        print(line[:-1]) 
    '''
    
main()
