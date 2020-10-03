from puzzle import Puzzle

#just some tests to show how the class works

#testPuzzle.printBoard()
#print(testPuzzle.getTile(0,2))

#stringVer = testPuzzle.printBoardString()
#print(stringVer)

testPuzzle = Puzzle([[1,2,3],[4,5,0],[6,7,8]])
wrongPuzzle = Puzzle([[4,2,1],[3,7,8],[6,5,0]])
testPuzzle2 = Puzzle([[1,2,3],[4,5,0],[6,7,8]])
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

print(testPuzzle.boardsEqual(wrongPuzzle.getBoard()))
print(testPuzzle.boardsEqual(testPuzzle2.getBoard()))

#testPuzzle.printBoard()