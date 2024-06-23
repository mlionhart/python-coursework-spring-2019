# Module 5
# Programming Assignment 6
# Prob-5.py

# Mike Hart

from graphics import *


def main():
    # creating graphical window
    win = GraphWin("Problem 5", 700, 400)
    # Creating coordinate structure for the body/frame, bumpers, roof, and wheels
    frame = Rectangle(Point(100, 300), Point(600, 200))
    frame.setOutline('red')
    frontBumper = Rectangle(Point(80, 300), Point(100, 260))
    frontBumper.setOutline('red')
    frontBumper.setFill('black')
    rearBumper = Rectangle(Point(600, 300), Point(620, 260))
    rearBumper.setOutline('red')
    rearBumper.setFill('black')
    roof = Polygon(Point(190, 200), Point(270, 100), Point(440, 100), Point(510, 200))
    roof.setOutline('red')
    wheel1 = Circle(Point(200, 310), 60)
    wheel1.setFill('black')
    wheel1.setOutline('red')
    wheel2 = Circle(Point(500, 310), 60)
    wheel2.setOutline('red')
    wheel2.setFill('black')
    # drawing the aforementioned items
    frame.draw(win)
    frontBumper.draw(win)
    rearBumper.draw(win)
    roof.draw(win)
    wheel1.draw(win)
    wheel2.draw(win)
    # Constructing lines for window 1 (I would have used a polygon for these,
    # but the instructions require at least some lines, so I used lines here)
    line1 = Line(Point(220, 190), Point(280, 110))
    line2 = Line(Point(280, 110), Point(360, 110))
    line3 = Line(Point(360, 110), Point(360, 190))
    line4 = Line(Point(220, 190), Point(360, 190))
    # Constructing lines for window 2
    line5 = Line(Point(370, 190), Point(370, 110))
    line6 = Line(Point(370, 110), Point(430, 110))
    line7 = Line(Point(430, 110), Point(480, 190))
    line8 = Line(Point(370, 190), Point(480, 190))
    # drawing aforementioned window lines to the screen
    line1.draw(win)
    line2.draw(win)
    line3.draw(win)
    line4.draw(win)
    line5.draw(win)
    line6.draw(win)
    line7.draw(win)
    line8.draw(win)
    # Waiting for user click to exit, then closing the window
    win.getMouse()
    win.close()


main()