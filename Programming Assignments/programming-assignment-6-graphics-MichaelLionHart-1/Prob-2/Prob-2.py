# Module 5
#   Programming Assignment 6
#       Prob-2.py

# Mike Hart

from graphics import *

def main():
     # Create Graphics Window that is 300 x 300 pixels
     win = GraphWin("Problem 2", 300, 300)
     # Create Square using Rectangle shape and set fill and outline to red
     shape = Rectangle(Point(25, 25), Point(75, 75))
     shape.setOutline("red")
     shape.setFill("red")
     shape.draw(win)
     # For loop to obtain mouse click coordinates 5 consecutive times
     # and Calculating new square location based on mouse position
     # and shape center (and adjusting 25 pixels, respectively, for 
     # placement of lower left corner of square at mouse click)
     for i in range(5):
          p = win.getMouse()
          c = shape.getCenter()
          dx = p.getX() - c.getX() + 25
          dy = p.getY() - c.getY() - 25
          shape.move(dx,dy)
     # Waiting for mouse click while showing a message to click once, 
     # and then click once more to begin second for loop (second click
     # is first loop of for loop)
     message1 = Text(Point(150, 10), "Click twice begin second for loop")
     message1.draw(win)
     win.getMouse()
     message1.undraw()
     # Initiating second for loop, the same as the last, except the 
     # calculations have been adjusted for the center position of the 
     # shape to be at mouse click location
     for i in range(5):
          p = win.getMouse()
          c = shape.getCenter()
          dx = p.getX() - c.getX()
          dy = p.getY() - c.getY()
          shape.move(dx,dy)
     # Printing second message, waiting for mouse click to finally
     # close window and end the program
     message2 = Text(Point(150, 10), "Click again to quit")
     message2.draw(win)
     win.getMouse()
     win.close()

main()