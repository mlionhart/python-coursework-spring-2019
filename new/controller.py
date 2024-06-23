# Controller.py
#
# For TicTacToe

from View import View
from Model import Model 

class Controller:

    def __init__(self):
       
        v = View()
        m = Model()
        selection = m.cellSelection(v.getClick())
        
        



        v.startText("Player X's turn")
        m.cellSelection(v.getClick())
        print(selection)
        if selection is False:
            v.startText("Pick another cell")
        v.drawSymbol("PlayerX")
        v.startText("Player O's Turn")


        
        input()  

   
def ControllerTest():
    c  = Controller()
    input()
        

if __name__ == "__main__":
    ControllerTest()