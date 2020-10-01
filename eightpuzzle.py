class Puzzle:
    def __init__(self, boardDefinition):
        self.board = boardDefinition #board is a 3x3 array (technically a list, but w/e)

    #Takes in itself, checks the board, and returns bool if the goal state or not
    def isGoal(self):
        return False

    #Takes in itself, returns list of possible moves to make
    #each move is a new Puzzle object
    def getNeighbors(self):
        pass

    #Returns the Hamming code for itself
    def getHamming(self):
        pass

    #Takes in row and column, returns the value at that spot
    def getTile(self,row,col):
        pass

    #Takes in a different board, returns true if the same, false otherwise
    def boardsEqual(self, boardToCheck):
        pass

    #Prints the board out in text
    def printBoard(self):
        pass


