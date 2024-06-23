from graphics import *
import random

def mousey():
    win = GraphWin("Mousey", 600, 600)
    for click in range(10):
        p = win.getMouse()
        randomNum = random.randint(5, 100)
        circ = Circle(p, randomNum)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        print(r, g, b)
        circ.setFill(color_rgb(r, g, b))
        circ.draw(win)
        print("Click", click, ":", p.getX(), p.getY())
    win.close()

mousey()

        