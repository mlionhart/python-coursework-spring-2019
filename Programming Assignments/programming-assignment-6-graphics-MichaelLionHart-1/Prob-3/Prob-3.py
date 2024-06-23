# Module 5
# Programming Assignment 6
# Prob-3.py

# Mike Hart

# Algorithm:  I started with the white circle, and each consecutive circle
# I subtracted the yellow circle's radius from the current circle's radius.
# Obviously keeping every circle's center point the same throughout the process.

from graphics import *


def main():
    win = GraphWin("Problem 3", 300, 300)
    circ5 = Circle(Point(150, 150), 100)
    circ5.setOutline('black')
    circ5.draw(win)
    circ4 = Circle(Point(150, 150), 80)
    circ4.setFill('black')
    circ4.draw(win)
    circ3 = Circle(Point(150, 150), 60)
    circ3.setFill('blue')
    circ3.draw(win)
    circ2 = Circle(Point(150, 150), 40)
    circ2.setFill('red')
    circ2.draw(win)
    circ1 = Circle(Point(150, 150), 20)
    circ1.setFill('yellow')
    circ1.draw(win)
    win.getMouse()
    win.close()

main()    