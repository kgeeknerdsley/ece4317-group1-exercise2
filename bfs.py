from puzzle import Puzzle

#perform depth first search!

#just some tests to show how the class works
testPuzzle = Puzzle([[1,2,3],[4,5,0],[6,7,8]])
testPuzzle.printBoard()
print(testPuzzle.getTile(0,2))

stringVer = testPuzzle.printBoardString()
print(stringVer)
