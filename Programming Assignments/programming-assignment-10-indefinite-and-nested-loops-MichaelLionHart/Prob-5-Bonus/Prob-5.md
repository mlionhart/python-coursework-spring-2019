# Module 7 - Programming Assignment 10 - Problem 5 OPTIONAL BONUS

**Specification**

Write a program using an event loop (see p. 272-273 in Zelle) that replicates the behavior in problem 1 of Programming Assignment 6 (the one with the red balls that move around the window). Follow the instructions below:

1. Create a window titled "Event Loop" that is 500 x 500
2. Use getMouse() to get the first point
3. Draw the initial circle
4. You will need a count variable (set to 1) and a Boolean variable, endFlag, set to False
5. Create your while True: loop
6. Inside the loop, call checkMouse()
7. If checkMouse() returns a point 
    - call a function "handleClick(win, circ, count, pt)"
        - if count <= 5
            - the function should calculate the dx, and dy values
            - the function should call the move method of circ
            - return False
        - else return true to end the program
    - update the count
8. Break out of the event loop when the endFlag is True
9. Close the window

The program should close cleaning, i.e. no exceptions.