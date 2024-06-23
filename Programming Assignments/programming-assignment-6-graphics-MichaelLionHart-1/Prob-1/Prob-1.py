# Module 5
#   Programming Assignment 6
#       Prob-1.py

# Mike Hart

# INSTRUCTIONS:
#   Insert a comment above each line of code in the program below to describe
#   what the code does

# Making graphics library available
from graphics import *

# calling function main()
def main():
     # The GraphWin() function creates a new window on the screen.  
     # It has been assigned to the 'win' variable, so we can manipulate
     # the window object through this variable
     win = GraphWin()
     # Draw a red circle, with a red outline centered at point (50, 50) with a radius of 20
     shape = Circle(Point(50,50), 20)
     shape.setOutline("red") # give circle a red outline
     shape.setFill("red") # color circle red
     shape.draw(win) # draw the circle

     for i in range(5): # iterate through a for loop, to execute the following code 5 times
          p = win.getMouse() # grab user mouse click coordinates, and assign to variable 'p'
          c = shape.getCenter() # find the center of the 'shape' object, and assign in to variable 'c'
          dx = p.getX() - c.getX() # subtract the x coordinate of 'c' from the x cooridinate of 'p', and assign value to variable 'dx'
          dy = p.getY() - c.getY() # subtract the y coordinate of 'c' from the y cooridinate of 'p', and assign value to variable 'dy'
          shape.move(dx,dy) # move 'shape' object dx-pixels on the x-axis, and dy-pixels on the y-axis
     win.close() # close the GraphWin window

main() # Run function main()