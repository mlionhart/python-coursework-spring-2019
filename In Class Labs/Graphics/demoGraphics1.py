from graphics import *


def main():
    win = GraphWin("Bill", 600, 600)

    p1 = Point(50, 50)
    p2 = Point(100, 100)
    r1 = Rectangle(p1, p2)
    r1.draw(win)

    r2 = Rectangle(Point(200, 200), Point(250, 250))
    r2.draw(win)

    input()

main()    