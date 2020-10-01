from puzzle import Puzzle

#perform breadth first search!

#just some tests to show how the class works

#testPuzzle.printBoard()
#print(testPuzzle.getTile(0,2))

#stringVer = testPuzzle.printBoardString()
#print(stringVer)

testPuzzle = Puzzle([[1,2,3],[4,5,0],[6,7,8]])
print("Unmodified board")
testPuzzle.printBoard()

print("Attempting to find neighbors")
possibilities = testPuzzle.getNeighbors()
print(possibilities)

#testPuzzle.printBoard()
