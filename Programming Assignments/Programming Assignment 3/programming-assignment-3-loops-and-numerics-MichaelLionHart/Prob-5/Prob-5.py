# Module 2
#   Programming Assignment 3
#     Prob-5.py

# Mike Hart

# **The Problem: Print a Receipt**
# - You purchased the following:
#     - 2 slices of pizza at $2.00 per slice
#     - 1 large Coke at $1.50
#     - 2 donuts at $0.56 each
def student():
    import math
    pizzaCost = float(4.00)
    cokeCost = float(1.50)
    donutsCost = float(1.12)
    subTotal = pizzaCost + cokeCost + donutsCost
    tax = round((subTotal * .084),2)
    total = round((subTotal + tax),2)
    
# - print the items purchased and their cost, one item per line
    print("Pizza x 2:\t", pizzaCost)
    print("Drink:\t\t", cokeCost)
    print("Donut x 2:\t", donutsCost)
# - print the total of all items
    print()
    print("Subtotal:\t", subTotal)
# - print the sales tax (8.4% of the total)
    print("Tax:\t\t", tax)
    print()
# - print the grand total
    print("Total:\t\t", total)
    print()
# - ask the user to enter an amount
    tendered = float(input("Enter amount to be tendered"))
# - print the amount tendered
    print("Tendered:\t", tendered)
# - print the change due
    change = round((tendered - total),2)
    print("Change:\t\t", change)
student()

# Output that meets the requirements is shown below. Note: your's does not have to match exactly. This is some room for you to show your own preferences/design. At a minimum, the output would show the numbers in order. After that it is up to you.

# ```
# Pizza @ 2:       4.0
# Drink:           1.5
# Donut @ 2:       1.12
# ----------------------
# Subtotal:        6.62
# Tax:             0.56

# Total:           7.18

# Please enter an amount: 10
# Tendered:       10.00
# Change:         2.82
# ```
