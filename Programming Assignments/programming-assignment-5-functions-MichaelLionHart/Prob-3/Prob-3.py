# Module 4
#   Programming Assignment 5
#       Prob-3.py

# Mike Hart

# Inputs: jobSize, paintCost (input by user prompt), $99 fee
# Processing: Calculating paint gallons, hours required, total paint cost, labor cost, and finally total cost of estimate
# Outputs: Printing the total cost for the estimate




def main():
    jobSize = eval(input('Enter job size in square feet :'))
    paintCost = eval(input('Enter the cost of paint per gallon :'))
    print('The Estimate for a job size of', jobSize, 'square feet is :', calculateEstimate(jobSize, paintCost))


def calculateEstimate(jobSize, paintCost):
    paintGal = jobSize // 12
    hours = (jobSize / 112) * 8
    totalPaintCost = paintGal * paintCost
    laborCost = hours * 35
    fee = 99
    totalEstimate = totalPaintCost + laborCost + fee
    return totalEstimate


main()
