# comments

from graphics import *

def main():
    # create a window
    win = GraphWin('Celsius Converter', 400, 300)

    # want text to align vertically
    stringTop = 'Celsius Temperature'
    stringBottom = 'Fahrenheit Temperature'

    # create text objects
    Text(Point(150, 50), stringTop).draw(win)
    Text(Point(150, 250), stringBottom).draw(win)

    # create "button"
    Rectangle(Point(125, 100), Point(275, 200)).draw(win)

    # create text inside box
    button = Text(Point(200, 150), 'Convert It')
    button.draw(win)

    inputField = Entry(Point(300, 50), 5)    
    inputField.setText("")
    inputField.draw(win)

    outputField = Text(Point(300, 250), '')
    outputField.draw(win)
    
    # wait for user click
    win.getMouse()

    # calculations
    celsius = float(inputField.getText())
    fahrenheit = (9.0/5.0) * celsius + 32

    # display result
    outputField.setText(round(fahrenheit, 2))

    # update button text
    button.setText('Quit')

    win.getMouse()

    input()

main()