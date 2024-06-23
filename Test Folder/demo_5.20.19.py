from graphics import *


def main():
    # sum = 0
    # count = 0
    # done = False
    # while not done:
    #     x = eval(input('Enter a non-negative number: '))
    #     if x < 0:
    #         done = True
    #     else:
    #         sum = sum + x
    #         count = count + 1

    # print('\nAverage:', sum/count)

    # while True:
    #     number = float(input("Enter a positive number: "))
    #     if number >= 0:
    #         break  # Exit loop if number is valid

    def handleClick(win, pt):
        print('click')

    def handleKey(win, key):
        print(key)

    win = GraphWin()

    # Event loop
    while True:
        key = win.checkKey()

        # detect termination
        if key == 'q':
            break

        if key:
            handleKey(win, key)

        pt = win.checkMouse()
        if pt:
            handleClick(win, pt)

    # clean up
    win.close()

main()
