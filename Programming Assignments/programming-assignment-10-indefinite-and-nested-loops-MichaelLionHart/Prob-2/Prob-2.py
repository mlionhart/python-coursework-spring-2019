# Module 7
#   Programming Assignment 10
#     Prob-2.py

# Mike Hart


def main():
    fileName = 'Prob-2\Prob-2-Input.txt'
    infile = open(fileName,'r')
    sum = 0.0
    line = infile.readline()
    while line != "":
        line = line.rstrip()
        line = line.split()
        for i in range(len(line)):
            print(line[i])
            sum = sum + float(line[i])
        line = infile.readline()
    print("\nThe sum of the numbers is", sum)   


main()    