class Puzzle:
    def __init__(self, boardData):
        self.board = boardData #board is a 3x3 array (technically a list, but w/e)

    #TODO: FILL OUT
    #Takes in itself, checks the board, and returns bool if the goal state or not
    def isGoal(self):
        return False

    #TODO: FILL OUT
    #Takes in itself, returns list of possible moves to make
    #TODO: should each new neighbor be a new object, or just return a list of the boards to check out?
    def getNeighbors(self):
        pass

    #TODO: FILL OUT
    #Returns the Hamming code for itself
    def getHamming(self):
        pass

    #Takes in row and column, returns the value at that spot
    def getTile(self,row,col):
        return self.board[row][col]

    #TODO: FILL OUT
    #Takes in a different board, returns true if the same, false otherwise
    def boardsEqual(self, boardToCheck):
        pass

    #Prints the board out in text
    def printBoard(self):
        for row in self.board:
            print(row)

    #Returns a coherent string of the board, for mapping purposes
    def printBoardString(self):
        tempString = ""

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                tempString += str(self.board[row][col]) + " "
            tempString += "\n"

        return tempString