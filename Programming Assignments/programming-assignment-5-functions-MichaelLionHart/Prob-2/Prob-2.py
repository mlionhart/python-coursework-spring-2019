# Module 4
#   Programming Assignment 5
#       Prob-2.py

# Mike Hart

# Inputs: Cost, tendered amount
# Processing: calculating change, dollars, pennies, quarters, dimes, and nickels
# Outputs: Printing change, dollars, pennies, quarters, dimes, and nickels

def calculateChange(change):
    import math
    dollars = (change * 100) // 100
    pennies = round(((change * 100) - (dollars * 100)) % 5)
    quarters = ((change * 100) - (dollars * 100)) // 25
    dimes = ((change * 100) - (dollars * 100) - (quarters * 25)) // 10
    nickels = ((change * 100) - (dollars * 100) - (quarters * 25) - (dimes * 10)) // 5
    print('Dollars: ', dollars)
    print('Quarters: ', quarters)
    print('Dimes: ', dimes)
    print('Nickels: ', nickels)
    print('Pennies: ', pennies)


def main():
    cost = eval(input('Enter cost: '))
    tendered = eval(input('Enter Amount Tendered: '))
    change = tendered - cost
    print()
    print('cost: ', cost, 'tendered :', tendered, 'change :', change)
    calculateChange(change)


main()
