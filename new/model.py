# Model.py
#
# For TicTacToe


from View import View


boarD = ["","","",
        "","",""
        "","","", ""]


class Model:

    def __init__(self):
        self._model = Model
       
       

    # populated board list to track player moves. Validates if cell is already populated through if loop
    def cellSelection(self,cell):

        board = boarD
        
        
        
        if cell == "cell1" and board[0] == "":
            board[0] = "X"
            return True
        elif cell == "cell1" and board[0] != "":
            return False
        elif cell == "cell2" and board[1] == "":
            board[1] = "X"
            return True
        elif cell == "cell2" and board[1] != "":
            return False
        elif cell == "cell3" and board[2] == "":
            return True
        elif cell == "cell3" and board[2] != "":
            return False
        elif cell == "cell4" and board[3] == "":
            return True
        elif cell == "cell4" and board[3] != "":
            return False
        elif cell == "cell5" and board[4] == "":
            return True
        elif cell == "cell5" and board[4] != "":
            return False
        elif cell == "cell6" and board[5] == "":
            return True
        elif cell == "cell6" and board[5] != "":
            return False
        elif cell == "cell7" and board[6] == "":
            return True
        elif cell == "cell7" and board[6] != "":
            return False
        elif cell == "cell8" and board[7] == "":
            return True
        elif cell == "cell8" and board[7] != "":
            return False
        elif cell == "cell9" and board[8] == "":
            return True
        elif cell == "cell9" and board[8] != "":
            return False
        elif cell == "cell9" and board[9] == "":
            return True
        elif cell == "cell9" and board[9] != "":
            return False


       
        


# test
def ModelTest():
    m = Model()
    m.cellSelection("cell1")
    m.cellSelection("cell2")
    print(boarD)
    
    
    
    pass

if __name__ == "__main__":
    ModelTest()