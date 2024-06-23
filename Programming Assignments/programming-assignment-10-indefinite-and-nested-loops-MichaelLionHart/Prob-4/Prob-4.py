# Module 7
#   Programming Assignment 10
#     Prob-4.py

# Mike Hart


def main():
    balances = []
    rate = float(input("Enter an Interest Rate: "))
    infile = open('Prob-4/balances.txt', 'r')
    line = infile.readline()
    while line != "":
        balances.append(line)
        line = infile.readline()
    print(balances)
    infile.close()
    calc(balances, rate)
        

def calc(list, interestRate):
    newList = []
    for i in range(len(list)):
        newList.append(float(list[i]) * interestRate)
        i = i + 1
    print(newList)
    outfile = open('Prob-4/balances.txt', 'w')
    for i in range(len(newList)):
        outfile.write(float(newList[i]) + '\n')
        i = i + 1
    outfile.close()


main()    