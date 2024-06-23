# Module 5
#   Programming Assignment 6
#       Prob-6.py

# Mike Hart

from graphics import *


def main():
    win = GraphWin("Problem 6", 600, 600)
    # blue lego
    lego1Body = Rectangle(Point(70, 190), Point(280, 90))
    lego1Body.setWidth(3)
    lego1Body.setFill('blue')
    lego1Body.draw(win)

    lego1Nub1 = Rectangle(Point(78, 90), Point(100, 80))
    lego1Nub1.setFill('blue')
    lego1Nub1.setWidth(3)
    lego1Nub1.draw(win)

    lego1Nub2 = lego1Nub1.clone()
    lego1Nub2.draw(win)
    moveClone(lego1Nub2, 42, 0)

    lego1Nub3 = lego1Nub2.clone()
    lego1Nub3.draw(win)
    moveClone(lego1Nub3, 42, 0)

    lego1Nub4 = lego1Nub3.clone()
    lego1Nub4.draw(win)
    moveClone(lego1Nub4, 42, 0)

    lego1Nub5 = lego1Nub4.clone()
    lego1Nub5.draw(win)
    moveClone(lego1Nub5, 42, 0)

    # green lego
    lego2Body = Rectangle(Point(300, 190), Point(510, 90))
    lego2Body.setFill('green')
    lego2Body.setWidth(3)
    lego2Body.draw(win)

    lego2Nub1 = Rectangle(Point(308, 90), Point(330, 80))
    lego2Nub1.setFill('green')
    lego2Nub1.setWidth(3)
    lego2Nub1.draw(win)

    lego2Nub2 = lego2Nub1.clone()
    lego2Nub2.draw(win)
    moveClone(lego2Nub2, 42, 0)

    lego2Nub3 = lego2Nub2.clone()
    lego2Nub3.draw(win)
    moveClone(lego2Nub3, 42, 0)

    lego2Nub4 = lego2Nub3.clone()
    lego2Nub4.draw(win)
    moveClone(lego2Nub4, 42, 0)

    lego2Nub5 = lego2Nub4.clone()
    lego2Nub5.draw(win)
    moveClone(lego2Nub5, 42, 0)

    # yellow lego
    lego3Body = Rectangle(Point(70, 350), Point(280, 250))
    lego3Body.setFill('yellow')
    lego3Body.setWidth(3)
    lego3Body.draw(win)

    lego3Nub1 = Rectangle(Point(78, 250), Point(100, 240))
    lego3Nub1.setFill('yellow')
    lego3Nub1.setWidth(3)
    lego3Nub1.draw(win)

    lego3Nub2 = lego3Nub1.clone()
    lego3Nub2.draw(win)
    moveClone(lego3Nub2, 42, 0)

    lego3Nub3 = lego3Nub2.clone()
    lego3Nub3.draw(win)
    moveClone(lego3Nub3, 42, 0)

    lego3Nub4 = lego3Nub3.clone()
    lego3Nub4.draw(win)
    moveClone(lego3Nub4, 42, 0)

    lego3Nub5 = lego3Nub4.clone()
    lego3Nub5.draw(win)
    moveClone(lego3Nub5, 42, 0)

    # red lego
    lego4Body = Rectangle(Point(300, 350), Point(510, 250))
    lego4Body.setFill('red')
    lego4Body.setWidth(3)
    lego4Body.draw(win)

    lego4Nub1 = Rectangle(Point(308, 250), Point(330, 240))
    lego4Nub1.setFill('red')
    lego4Nub1.setWidth(3)
    lego4Nub1.draw(win)

    lego4Nub2 = lego4Nub1.clone()
    lego4Nub2.draw(win)
    moveClone(lego4Nub2, 42, 0)

    lego4Nub3 = lego4Nub2.clone()
    lego4Nub3.draw(win)
    moveClone(lego4Nub3, 42, 0)

    lego4Nub4 = lego4Nub3.clone()
    lego4Nub4.draw(win)
    moveClone(lego4Nub4, 42, 0)

    lego4Nub5 = lego4Nub4.clone()
    lego4Nub5.draw(win)
    moveClone(lego4Nub5, 42, 0)

    # light blue lego
    lego5Body = Rectangle(Point(70, 510), Point(280, 410))
    lego5Body.setFill('lightblue')
    lego5Body.setWidth(3)
    lego5Body.draw(win)

    lego5Nub1 = Rectangle(Point(78, 410), Point(100, 400))
    lego5Nub1.setFill('lightblue')
    lego5Nub1.setWidth(3)
    lego5Nub1.draw(win)

    lego5Nub2 = lego5Nub1.clone()
    lego5Nub2.draw(win)
    moveClone(lego5Nub2, 42, 0)

    lego5Nub3 = lego5Nub2.clone()
    lego5Nub3.draw(win)
    moveClone(lego5Nub3, 42, 0)

    lego5Nub4 = lego5Nub3.clone()
    lego5Nub4.draw(win)
    moveClone(lego5Nub4, 42, 0)

    lego5Nub5 = lego5Nub4.clone()
    lego5Nub5.draw(win)
    moveClone(lego5Nub5, 42, 0)

    # black lego
    lego6Body = Rectangle(Point(300, 510), Point(510, 410))
    lego6Body.setFill('black')
    lego6Body.setWidth(3)
    lego6Body.draw(win)

    lego6Nub1 = Rectangle(Point(308, 410), Point(330, 400))
    lego6Nub1.setFill('black')
    lego6Nub1.setWidth(3)
    lego6Nub1.draw(win)

    lego6Nub2 = lego6Nub1.clone()
    lego6Nub2.draw(win)
    moveClone(lego6Nub2, 42, 0)

    lego6Nub3 = lego6Nub2.clone()
    lego6Nub3.draw(win)
    moveClone(lego6Nub3, 42, 0)

    lego6Nub4 = lego6Nub3.clone()
    lego6Nub4.draw(win)
    moveClone(lego6Nub4, 42, 0)

    lego6Nub5 = lego6Nub4.clone()
    lego6Nub5.draw(win)
    moveClone(lego6Nub5, 42, 0)

    win.getMouse()
    win.close()


def moveClone(cloneName, x, y):
    dx = x
    dy = y
    cloneName.move(dx, dy)


main()