# Module 5 - Skill Building Exercise No. 9 Solution
# Author: Bruce Elgort
# Date: July 22, 2017

def main():
    print("This program calculates the future value of an investment.")
    print()
    
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annualized interest rate: "))
    years = eval(input("Enter the number of years: "))

    print("Year   Value")
    print("------------")
    for i in range(years+1):
        # use string formatting to make output align like sample provided
        print("{0:3}   ${1:7.2f}".format(i, principal))
        principal = principal * (1 + apr)

main()
