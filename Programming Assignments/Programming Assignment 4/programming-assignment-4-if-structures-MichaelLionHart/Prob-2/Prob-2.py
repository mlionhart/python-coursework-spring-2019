# Module 3
#   Programming Assignment 4
#     Prob-2.py

# Mike Hart

'''
Your IPO comment goes here

Input: Asks user for name, wage, and hours.

Process: Calculating regularWages, overtimeWages, totalWages, taxWithholding,
         insuranceWithholding, takeHomePay.

Output: Displaying (printing) Employee's name, Regular wages, Overtime wages, Total wages,
        Tax withholding, Insurance withholding, Take home pay.

'''

def main():
    name = input("Please enter your full name: ")
    wage = eval(input("Please enter your hourly wage: "))
    hours = eval(input("Please enter how many hours you worked this week: "))
    regularWages = wage * 40
    overtimeWages = (wage * 1.5) * (hours - 40)
    totalWages = regularWages + overtimeWages
    taxWithholding = totalWages * .2
    insuranceWithholding = totalWages * .1
    takeHomePay = totalWages - (taxWithholding + insuranceWithholding)
    print()
    print("Employee's Name:\t", name)
    print("Regular Wages:\t\t", regularWages)
    print("Overtime Wages:\t\t", overtimeWages)
    print("Total Wages:\t\t", totalWages)
    print("Tax Withholding:\t", taxWithholding)
    print("Insurance Withholding:\t", insuranceWithholding)
    print("Take Home Pay:\t\t", takeHomePay)

main()