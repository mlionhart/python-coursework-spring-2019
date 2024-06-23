# Module 5
#   Programming Assignment 6
#       Prob-4.py

# Mike Hart

from graphics import *


def main():
    # Creating Graphic Window, then creating the house frame using
    # calculations based on the first two mouse clicks, then drawing it
    win = GraphWin("Problem 4", 300, 300)
    p1 = win.getMouse()
    p2 = win.getMouse()
    framePoint1 = Point(p1.getX(), p1.getY())
    framePoint2 = Point(p2.getX(), p2.getY())
    frame = Rectangle(framePoint1, framePoint2)
    frame.draw(win)
    # Using the third mouse click, creating the door, then drawing it
    p3 = win.getMouse()
    doorWidth = (p2.getX() - p1.getX()) / 5
    doorPoint1x = p3.getX() - (doorWidth / 2)
    doorPoint2x = p3.getX() + (doorWidth / 2)
    door = Rectangle(Point(doorPoint1x, p1.getY()), Point(doorPoint2x, p3.getY()))
    door.draw(win)
    # Using the fourth mouse click, creating the window, then drawing it
    p4 = win.getMouse()
    windowWidth = doorWidth / 2
    window1x = p4.getX() - (windowWidth / 2)
    window1y = p4.getY() + (windowWidth / 2)
    window2x = p4.getX() + (windowWidth / 2)
    window2y = p4.getY() - (windowWidth / 2)
    window = Rectangle(Point(window1x, window1y), Point(window2x, window2y))
    window.draw(win)
    # Using the fifth mouse click, creating the roof using the polygon object,
    # then drawing it to the window
    p5 = win.getMouse()
    roofPoint1 = Point(p5.getX(), p5.getY())
    roofPoint2 = Point(p1.getX(), p2.getY())
    roofPoint3 = Point(p2.getX(), p2.getY())
    roof = Polygon(roofPoint1, roofPoint2, roofPoint3)
    roof.draw(win)
    # Waiting for a final mouse click before ending (closing) the window
    win.getMouse()
    win.close()
    

main()