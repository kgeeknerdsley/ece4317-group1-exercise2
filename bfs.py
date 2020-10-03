from puzzle import Puzzle

#perform breadth first search!

#just some tests to show how the class works

#testPuzzle.printBoard()
#print(testPuzzle.getTile(0,2))

#stringVer = testPuzzle.printBoardString()
#print(stringVer)

testPuzzle = Puzzle([[1,2,3],[4,5,0],[6,7,8]])
wrongPuzzle = Puzzle([[4,2,1],[3,7,8],[6,5,0]])
print("\nCorrect board")
testPuzzle.printBoard()
print("\n")
print("Incorrect board")
wrongPuzzle.printBoard()

#print("Attempting to find neighbors")
#possibilities = testPuzzle.getNeighbors()
#print(possibilities)

print(testPuzzle.isGoal())
print(testPuzzle.getHamming())
print(wrongPuzzle.isGoal())
print(wrongPuzzle.getHamming())

#testPuzzle.printBoard()
