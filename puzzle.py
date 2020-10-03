import copy

class Puzzle:
    def __init__(self, boardData):
        self.board = boardData #board is a 3x3 array (technically a list, but w/e)

    #Takes in itself, checks the board, and returns bool if the goal state or not
    def isGoal(self):
        i = 1
        result = False

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if(self.board[row][col] == i):
                    i = i+1
                
        if(i == 9):
            result = True
        else:
            result = False

        return result

    #Takes in itself, returns list of possible moves to make
    def getNeighbors(self):
        neighborBoards = [] #holds all the new boards we make
        holeRow = 0
        holeCol = 0

        #find the hole in our board: DONE
        #check four possible moves: up, down, left, right
        #only calculate the move if we know it's legal

        #iterate over the array. when we find the hole, mark its location!
        for holeSearchR in range(len(self.board)):
            for holeSearchC in range(len(self.board[holeSearchR])):
                if(self.getTile(holeSearchR,holeSearchC) == 0):
                    holeRow = holeSearchR
                    holeCol = holeSearchC

        print("Hole located at (" + str(holeRow) + " " + str(holeCol) + ")\n")

        #attempt up move
        if(holeRow-1 >= 0):
            tempVal = self.getTile(holeRow-1, holeCol)
            copiedBoard = copy.deepcopy(self.board)
            copiedBoard[holeRow-1][holeCol] = 0
            copiedBoard[holeRow][holeCol] = tempVal
            neighborBoards.append(copiedBoard)
        
        #attempt left move
        if(holeCol-1 >= 0):
            tempVal = self.getTile(holeRow, holeCol-1)
            copiedBoard = copy.deepcopy(self.board)
            copiedBoard[holeRow][holeCol-1] = 0
            copiedBoard[holeRow][holeCol] = tempVal
            neighborBoards.append(copiedBoard)

        #attempt right move
        if(holeCol+1 <= 2):
            tempVal = self.getTile(holeRow, holeCol+1)
            copiedBoard = copy.deepcopy(self.board)
            copiedBoard[holeRow][holeCol+1] = 0
            copiedBoard[holeRow][holeCol] = tempVal
            neighborBoards.append(copiedBoard)

        #attempt right move
        if(holeRow+1 <= 2):
            tempVal = self.getTile(holeRow+1, holeCol)
            copiedBoard = copy.deepcopy(self.board)
            copiedBoard[holeRow+1][holeCol] = 0
            copiedBoard[holeRow][holeCol] = tempVal
            neighborBoards.append(copiedBoard)

        return neighborBoards

    #TODO: FILL OUT
    #Returns the Hamming code for itself
    def getHamming(self):
        pass

    #Takes in row and column, returns the value at that spot
    def getTile(self,row,col):
        return self.board[row][col]

    #change the tile for the entire board's object (will NOT preserve current board state)
    def changeTile(self, newValue, row, col):
        self.board[row][col] = newValue

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