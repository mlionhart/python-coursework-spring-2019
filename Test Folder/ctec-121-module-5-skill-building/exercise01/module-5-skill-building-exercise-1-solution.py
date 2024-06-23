# Module 5 - Skill Building Exercise No. 1 Solution
# Author: Bruce Elgort
# Date: July 22, 2017

def main():
    # get the day month and year
    day, month, year = eval(input("Please enter day, month, and year numbers: "))

    # use string formatting placeholders to assign variables to slots
    date1 = "{0}/{1}/{2}".format(day, month, year)

    # list of months
    months = ["January", "February", "March", "April", 
              "May", "June", "July", "August", 
              "September", "October", "November", "December"]

    # assign month based on value
    monthStr = months[month-1]
    # use string formatting
    date2 = "{0} {1}, {2} ".format(monthStr,day,year)
    # display results
    print("The date is {0} or {1}".format(date1, date2))

main()